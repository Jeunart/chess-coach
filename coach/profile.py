"""Profil durable de l'élève, toutes cadences, avec fenêtres 7 / 30 / 90 jours."""
import collections
import datetime

from coach import facts, report


def _rate(gs):
    return sum(1 for g in gs for e in g["errs"] if report.decisive(e)) / max(len(gs), 1)


def _window(games, today, days, offset=0):
    hi = today - datetime.timedelta(days=offset)
    lo = hi - datetime.timedelta(days=days)
    return [g for g in games if lo < report.day(g) <= hi]


def _motifs(gs):
    return collections.Counter(facts.why_loss(e)["motif"] for g in gs for e in g["errs"] if report.decisive(e))


def build(games, today):
    L = ["# Profil durable de l'élève", "", f"Mis à jour le {today}. Toutes cadences (bullet, blitz, rapide, par correspondance).", ""]
    if not games:
        return L + ["Aucune partie analysée."]
    L += ["## Par cadence"]
    for tc in ("rapid", "blitz", "bullet", "daily"):
        gs = [g for g in games if g["tc"] == tc]
        if not gs:
            continue
        old = [g for g in gs if report.day(g) <= today - datetime.timedelta(days=30)]
        w = sum(g["result"] == "win" for g in gs)
        L.append(f"- {report.TC_FR[tc].capitalize()} : {len(gs)} parties, {100 * w // len(gs)} % de victoires, "
                 f"classement actuel {gs[-1]['rating']}" + (f" (il y a 30 jours : {old[-1]['rating']})" if old else ""))
    L += ["", "## Erreurs décisives par partie (perte d'au moins 2 pions, position pas déjà perdue)"]
    for days in (7, 30, 90):
        w = _window(games, today, days)
        if w:
            L.append(f"- {days} derniers jours : {_rate(w):.1f} ({len(w)} parties)")
    prev = _window(games, today, 30, 30)
    cur = _window(games, today, 30)
    if prev and cur:
        trend = "en hausse" if _rate(cur) > _rate(prev) + 0.2 else "en baisse" if _rate(cur) < _rate(prev) - 0.2 else "stable"
        L.append(f"- Tendance : {_rate(cur):.1f} sur 30 jours contre {_rate(prev):.1f} sur les 30 jours précédents ({trend})")
    L += ["", "## Types d'erreurs décisives (30 derniers jours / total)"]
    m30, mall = _motifs(cur), _motifs(games)
    for m, c in mall.most_common():
        L.append(f"- {facts.MOTIFS[m]} : {m30.get(m, 0)} / {c} (étiquettes automatiques, approximatives)")
    L += ["", "## Phase de la partie"]
    ph = collections.Counter(e["phase"] for g in games for e in g["errs"] if report.decisive(e))
    L += [f"- {p} : {c}" for p, c in ph.most_common()]
    pressure = sum(1 for g in games for e in g["errs"] if report.decisive(e) and e.get("clk") is not None and e["clk"] < 60)
    L += ["", "## Gestion du temps", f"- Erreurs décisives avec moins d'une minute à l'horloge : {pressure}"]
    missed = [g for g in games if g["result"] != "win" and max((x for x in [(1 if g["white"] else -1) * v for v in g["ev"]]), default=0) >= 300]
    L += ["", "## Avantages non convertis",
          f"- Parties non gagnées où tu as eu au moins 3 pions d'avantage : {len(missed)} sur {len(games)}"]
    L += [f"  - {g['url']} ({report.day(g)}, {report.outcome(g)} {report.ending(g)})" for g in missed[-3:]]
    L += ["", "## Ouvertures les plus jouées (victoires/nulles/défaites)"]
    for white, label in ((True, "blancs"), (False, "noirs")):
        ops = collections.defaultdict(collections.Counter)
        for g in games:
            if g["white"] == white:
                ops[g.get("opening", "inconnue")][report.outcome(g)] += 1
        for name, c in sorted(ops.items(), key=lambda kv: -sum(kv[1].values()))[:4]:
            L.append(f"- {label}, {name} : {c['victoire']}/{c['nulle']}/{c['défaite']}")
    return L + [""]
