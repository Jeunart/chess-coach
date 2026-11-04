"""Génère seance.md, corriges.md, rapport.md, profil.md (+ archives datées) depuis data/v2.

python -m coach.render [AAAA-MM-JJ]   (date du jour par défaut, fuseau Europe/Zurich)
"""
import collections
import datetime
import json
import os
import random
import sys

from coach import bilan, facts, profile, report

DATA = "data/v2/games.jsonl"
MANIFEST = "data/v2/manifest.json"
LESSON_BY_MOTIF = {"piece_en_prise": "L01", "menace_ignoree": "L02", "gain_rate": "L03",
                   "fourchette_subie": "L04", "mat_subi": "L06", "mat_rate": "L06", "autre": "L13"}
LESSON_TITLE = {"L01": "Mes pièces sont-elles protégées ?", "L02": "Que veut faire mon adversaire ?",
                "L03": "Échecs, prises, menaces : ne pas laisser de cadeau", "L04": "Les fourchettes",
                "L06": "Sécurité du roi et mats en 1 ou 2 coups", "L13": "Calculer trois coups à l'avance",
                "L17": "Gérer son temps"}


def load(root="."):
    games = []
    path = os.path.join(root, DATA)
    if os.path.exists(path):
        games = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    mpath = os.path.join(root, MANIFEST)
    manifest = json.load(open(mpath, encoding="utf-8")) if os.path.exists(mpath) else {}
    return sorted(games, key=lambda g: g["end"]), manifest


def pick_positions(day_games, all_games, today, n=4, n_revisit=2):
    """Positions de la séance : une erreur décisive par partie de la veille (la plus lourde, thèmes variés),
    puis révision d'erreurs d'il y a 3, 7 et 14 jours (répétition espacée sans état à conserver)."""
    cands = []
    for g in day_games:
        es = [e for e in g["errs"] if report.decisive(e, -150)]
        if es:
            e = max(es, key=lambda x: x["loss"])
            cands.append((min(e["loss"], 800), g, e, facts.why_loss(e)["motif"]))
    cands.sort(key=lambda t: -t[0])
    chosen, per_motif = [], collections.Counter()
    for _, g, e, m in cands:
        if per_motif[m] < 2 and len(chosen) < n:
            chosen.append((g, e))
            per_motif[m] += 1
    yesterday = today - datetime.timedelta(days=1)
    revisit = []
    for off in (3, 7, 14):
        d = yesterday - datetime.timedelta(days=off)
        es = [(g, e) for g in all_games if report.day(g) == d for e in g["errs"] if report.decisive(e, -150)]
        if es:
            revisit.append((off,) + max(es, key=lambda t: t[1]["loss"]))
    if not revisit:
        pool = [(g, e) for g in all_games if report.day(g) < yesterday for e in g["errs"]
                if report.decisive(e, -150) and (yesterday - report.day(g)).days <= 30]
        if pool:
            g, e = random.Random(str(today)).choice(pool)
            revisit.append(((yesterday - report.day(g)).days, g, e))
    return chosen, revisit[:n_revisit]


def lesson_of(day_games, all_games, today):
    pool = [e for g in day_games for e in g["errs"] if report.decisive(e)]
    if len(pool) < 2:
        since = today - datetime.timedelta(days=30)
        pool = [e for g in all_games if report.day(g) >= since for e in g["errs"] if report.decisive(e)]
    if not pool:
        return "L13", "aucune erreur décisive récente"
    if sum(1 for e in pool if e.get("clk") is not None and e["clk"] < 60) >= max(3, len(pool) // 2):
        return "L17", "la majorité de tes erreurs décisives arrivent avec moins d'une minute à l'horloge"
    c = collections.Counter(facts.why_loss(e)["motif"] for e in pool)
    c.pop("autre", None) if len(c) > 1 else None
    motif, k = c.most_common(1)[0]
    return LESSON_BY_MOTIF[motif], f"{k} erreur(s) décisive(s) récente(s) de type « {facts.MOTIFS[motif]} »"


def decisive_rate(gs):
    return sum(1 for g in gs for e in g["errs"] if report.decisive(e)) / max(len(gs), 1)


def check_block(games_y, manifest, today):
    L = ["## Contrôle des données"]
    if not manifest:
        return L + ["- ⚠ Aucun manifeste d'import : données non vérifiées.", ""]
    fails = manifest.get("echecs", [])
    L.append(f"- Parties importées au total : {sum(manifest.get('total', {}).values())} "
             f"({', '.join(f'{k} {v}' for k, v in sorted(manifest.get('total', {}).items()))})")
    L.append(f"- Parties de la veille importées et analysées : {len(games_y)}")
    if manifest.get("exclues"):
        L.append(f"- Hors périmètre (variantes, etc.) : {sum(manifest['exclues'].values())}")
    if fails:
        L.append(f"- ⚠ ANALYSE INCOMPLÈTE : {len(fails)} partie(s) en échec ({', '.join(fails[:5])}). Ne pas présenter ce rapport comme complet.")
    L.append("- Les données publiques de chess.com peuvent avoir jusqu'à 12 h de retard : une partie tardive apparaîtra dans le rapport suivant.")
    return L + [""]


def render(today, root="."):
    games, manifest = load(root)
    yesterday = today - datetime.timedelta(days=1)
    gy = [g for g in games if report.day(g) == yesterday]
    fallback = False
    if not gy and games:
        last = report.day(games[-1])
        gy, fallback = [g for g in games if report.day(g) == last], True
    ts = datetime.datetime.now(report.TZ).strftime("%Y-%m-%d %H:%M")
    day_label = report.day(gy[0]) if gy else yesterday
    chosen, revisit = pick_positions(gy, games, today)
    lesson, why = lesson_of(gy, games, today)
    since30 = today - datetime.timedelta(days=30)
    g30 = [g for g in games if report.day(g) >= since30]

    S = [f"# Séance du {today}", "", f"Généré le {ts} (heure de Zurich). Parties étudiées : celles du {day_label}.", ""]
    if fallback:
        S += [f"⚠ Aucune partie le {yesterday} : la séance porte sur le dernier jour joué ({day_label}).", ""]
    S += check_block(gy, manifest, today)
    S += ["## Bilan", f"- Parties du {day_label} : {len(gy)} "
          + (f"({', '.join(f'{k} {v}' for k, v in collections.Counter(g['tc'] for g in gy).items())})" if gy else ""),
          f"- Résultats : {sum(g['result'] == 'win' for g in gy)} victoire(s), "
          f"{sum(g['result'] in report.DRAW for g in gy)} nulle(s), "
          f"{sum(g['result'] != 'win' and g['result'] not in report.DRAW for g in gy)} défaite(s)"]
    for tc in ("rapid", "blitz", "bullet", "daily"):
        t = [g for g in gy if g["tc"] == tc]
        if t:
            S.append(f"- Classement {report.TC_FR[tc]} : {t[0]['rating']} -> {t[-1]['rating']}")
    S += [f"- Erreurs décisives par partie : {decisive_rate(gy):.1f} ce jour-là, {decisive_rate(g30):.1f} sur 30 jours", ""]
    S += ["## Parties de la veille (récit, sans les solutions)"]
    for i, g in enumerate(gy, 1):
        S += [f"{i}. {g['url']}"] + [f"   - {s}" for s in report.story(g)]
    S += ["", "## Positions de la séance",
          "Ouvre le lien Lichess (échiquier cliquable ; garde le moteur d'analyse éteint), "
          "pense à voix haute, puis joue ton coup. Les corrigés sont dans corriges.md.", ""]
    C = [f"# Corrigés de la séance du {today}", "", "À lire SEULEMENT après la réponse de l'élève, position par position.", ""]
    k = 0
    for g, e in chosen:
        k += 1
        S += report.question_block(k, g, e, "Position")
        C += report.solution_block(k, g, e, "Position")
    for off, g, e in revisit:
        k += 1
        S += report.question_block(k, g, e, "Position", f" (révision d'une erreur d'il y a {off} jours)")
        C += report.solution_block(k, g, e, "Position")
    if k == 0:
        S += ["Aucune position exploitable aujourd'hui : fais une revue libre des parties (rapport.md).", ""]
    S += [f"## Leçon du jour : {lesson} - {LESSON_TITLE.get(lesson, '')}",
          "(À annoncer APRÈS les positions : ce titre souffle le type d'erreur à chercher.)",
          f"Choisie parce que : {why}. Détail de la leçon dans programme.md.", "",
          "## Pour aller plus loin",
          "- bilan.md : bilan de la veille (rapides 10 et 15 min en focus, axes de progression, conseils) ; à lire quand l'élève demande l'analyse de la veille.",
          "- rapport.md : vue d'ensemble ; rapport/partie-N.md : analyse détaillée et expliquée de la partie N de la veille (contient les solutions : à ouvrir après les positions, ou à la demande de l'élève).",
          "- profil.md : profil durable et progression. programme.md : les leçons.", ""]

    RAW = "https://raw.githubusercontent.com/Jeunart/chess-coach/main/rapport/partie-{}.md"
    R = [f"# Rapport du {today} : vue d'ensemble", "", f"Généré le {ts} (heure de Zurich). Parties du {day_label}.",
         "Chaque partie a son fichier détaillé (récit, moments clés, solutions). Lis seulement celui de la partie demandée.", ""]
    R += check_block(gy, manifest, today)
    R += ["## Parties"]
    for i, g in enumerate(gy, 1):
        R.append(f"- Partie {i} : {report.TC_FR[g['tc']]}, {report.outcome(g)} {report.ending(g)}, "
                 f"{sum(1 for e in g['errs'] if report.decisive(e))} erreur(s) décisive(s) - détail : {RAW.format(i)} - {g['url']}")
    R.append("")
    recent = day_label - datetime.timedelta(days=3)  # évite de tout lister lors du premier import
    late = [g for g in games if g.get("seen") == str(today) and recent <= report.day(g) < day_label]
    if late:
        R += ["## Parties arrivées en retard (jours précédents)"] + [f"- {g['url']} ({report.day(g)})" for g in late] + [""]

    out = {"seance.md": S, "corriges.md": C, "rapport.md": R, "profil.md": profile.build(games, today),
           "bilan.md": bilan.build(gy, games, today)}
    rdir = os.path.join(root, "rapport")
    os.makedirs(rdir, exist_ok=True)
    for f in os.listdir(rdir):
        if f.startswith("partie-"):
            os.remove(os.path.join(rdir, f))  # un seul jeu de fichiers à la fois ; l'historique est dans archives/
    for i, g in enumerate(gy, 1):
        out[f"rapport/partie-{i}.md"] = [f"# Partie {i} du {day_label}", ""] + report.game_section(i, g)
    for name, lines in out.items():
        text = "\n".join(lines) + "\n"
        open(os.path.join(root, name), "w", encoding="utf-8").write(text)
        arch = os.path.join(root, "archives", str(today), name)
        os.makedirs(os.path.dirname(arch), exist_ok=True)
        open(arch, "w", encoding="utf-8").write(text)
    return out


if __name__ == "__main__":
    d = datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.datetime.now(report.TZ).date()
    render(d)
    print("rendu OK pour", d)
