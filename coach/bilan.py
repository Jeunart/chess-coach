"""Bilan de la veille : toutes les parties du jour, focus sur les rapides de 10 et 15 minutes.

Tout est calculé par le code à partir des données vérifiées. Le coach (ChatGPT) raconte et explique,
il ne recalcule rien. Numérotation des parties = celle de rapport/partie-N.md.
"""
import collections
import datetime

import chess

from coach import facts, report

FOCUS_BASES = (600, 900)  # 10 et 15 minutes (avec ou sans incrément)
RAW = "https://raw.githubusercontent.com/Jeunart/chess-coach/main/rapport/partie-{}.md"

ADVICE = {
    "piece_en_prise": "Avant chaque coup, deux questions : « La pièce que je déplace est-elle défendue ? "
                      "Qu'est-ce que mon coup laisse sans défense ? »",
    "menace_ignoree": "Avant de jouer, regarde le dernier coup adverse : qu'attaque-t-il, ou que prépare-t-il ?",
    "gain_rate": "Quand tu es mieux, cherche d'abord les échecs, les prises et les pièces non défendues avant de jouer un coup tranquille.",
    "fourchette_subie": "Avant de poser une pièce, regarde si un cavalier adverse peut sauter sur une case qui attaque deux de tes pièces.",
    "mat_subi": "Quand le roi est exposé, regarde les échecs adverses (tous) avant chaque coup.",
    "mat_rate": "Avant de jouer, passe en revue tous tes échecs : un mat en 1 ou en 2 coups se trouve ainsi.",
    "autre": "Dans le calme, choisis un plan simple (développer, roquer, activer la dernière pièce) et vérifie que ton coup ne gêne pas tes pièces.",
}


def is_focus(g):
    if g["tc"] != "rapid":
        return False
    try:
        return int(str(g["ctrl"]).partition("+")[0]) in FOCUS_BASES
    except ValueError:
        return False


def _decisive(g):
    return [e for e in g["errs"] if report.decisive(e)]


def _max_adv(g):
    me = 1 if g["white"] else -1
    return max((me * v for v in g["ev"]), default=0)


def _san(e):
    try:
        return chess.Board(e["fen"]).san(chess.Move.from_uci(e["move_uci"]))
    except (ValueError, KeyError):
        return e.get("move_uci", "?")


def _rate(gs):
    return sum(len(_decisive(g)) for g in gs) / max(len(gs), 1)


def _motifs(gs):
    return collections.Counter(facts.why_loss(e)["motif"] for g in gs for e in _decisive(g))


def _game_lines(i, g):
    errs = report.key_errors(g, 4)
    n_dec = len(_decisive(g))
    gift_total, gift_taken = report.gifts(g)
    head = (f"- Partie {i} ({report.ctrl_fr(g['ctrl'])}, {'blancs' if g['white'] else 'noirs'}, "
            f"contre {g['opp_rating']}) : {report.outcome(g)} {report.ending(g)}. "
            f"Ouverture : {g.get('opening', 'inconnue')}. {n_dec} erreur(s) décisive(s). "
            f"Détail : {RAW.format(i)}")
    L = [head]
    for e in errs:
        m = facts.why_loss(e)["motif"]
        clk = f", horloge {report.clock(e['clk'])}" if e.get("clk") is not None else ""
        L.append(f"  - coup {e['n']} ({e['phase']}) : {_san(e)}, perte {e['loss'] / 100:.1f} pion(s), "
                 f"thème automatique : {facts.MOTIFS[m]}{clk}")
    if gift_total:
        L.append(f"  - cadeaux de l'adversaire saisis : {gift_taken} sur {gift_total}")
    if report.outcome(g) != "victoire" and _max_adv(g) >= 300:
        L.append(f"  - avantage non converti : jusqu'à +{_max_adv(g) / 100:.1f} pions, mais la partie n'a pas été gagnée")
    return L


def build(gy, games, today):
    day_label = report.day(gy[0]) if gy else today - datetime.timedelta(days=1)
    L = [f"# Bilan de la veille ({day_label})", "",
         "Calculé par le robot à partir des parties analysées (Stockfish). Les thèmes sont des étiquettes automatiques, approximatives.",
         "Le coach explique ces faits avec ses mots, sans rien recalculer.", ""]
    if not gy:
        return L + ["Aucune partie ce jour-là.", ""]

    L += ["## Vue d'ensemble"]
    for tc in ("rapid", "blitz", "bullet", "daily"):
        t = [g for g in gy if g["tc"] == tc]
        if t:
            w = sum(g["result"] == "win" for g in t)
            L.append(f"- {report.TC_FR[tc].capitalize()} : {len(t)} partie(s), {w} victoire(s), "
                     f"classement {t[0]['rating']} -> {t[-1]['rating']}, "
                     f"{_rate(t):.1f} erreur(s) décisive(s) par partie")
    L.append("")

    idx = {id(g): i for i, g in enumerate(gy, 1)}
    focus = [g for g in gy if is_focus(g)]
    L += ["## Focus : rapides 10 et 15 minutes"]
    if focus:
        L.append(f"- {len(focus)} partie(s) ce jour-là ; durées : "
                 + ", ".join(sorted({report.ctrl_fr(g['ctrl']) for g in focus})))
        if not any(int(str(g["ctrl"]).partition("+")[0]) == 900 for g in focus):
            L.append("- Aucune partie de 15 minutes ce jour-là.")
        for g in focus:
            L += _game_lines(idx[id(g)], g)
    else:
        L.append("- Aucune partie rapide de 10 ou 15 minutes ce jour-là.")
    other = [g for g in gy if not is_focus(g)]
    if other:
        L += ["", "## Autres parties du jour (résumé)"]
        for g in other:
            L.append(f"- Partie {idx[id(g)]} ({report.TC_FR[g['tc']]}, {report.ctrl_fr(g['ctrl'])}) : "
                     f"{report.outcome(g)} {report.ending(g)}, {len(_decisive(g))} erreur(s) décisive(s)")
    L.append("")

    since = today - datetime.timedelta(days=30)
    f30 = [g for g in games if is_focus(g) and report.day(g) >= since]
    L += ["## Rapides 10 et 15 min : tendance sur 30 jours"]
    if f30:
        w = sum(g["result"] == "win" for g in f30)
        L.append(f"- {len(f30)} parties, {100 * w // len(f30)} % de victoires, "
                 f"{_rate(f30):.1f} erreur(s) décisive(s) par partie, classement {f30[0]['rating']} -> {f30[-1]['rating']}")
        m30 = _motifs(f30)
        tot = sum(m30.values()) or 1
        L.append("- Types d'erreurs : " + ", ".join(f"{facts.MOTIFS[m]} {100 * c // tot} %" for m, c in m30.most_common(4)))
        ph = collections.Counter(e["phase"] for g in f30 for e in _decisive(g))
        L.append("- Phase des erreurs : " + ", ".join(f"{p} {c}" for p, c in ph.most_common()))
        pressure = sum(1 for g in f30 for e in _decisive(g) if e.get("clk") is not None and e["clk"] < 60)
        L.append(f"- Erreurs décisives avec moins d'une minute à l'horloge : {pressure} sur {tot}")
        missed = [g for g in f30 if g["result"] != "win" and _max_adv(g) >= 300]
        L.append(f"- Parties non gagnées avec au moins 3 pions d'avantage : {len(missed)} sur {len(f30)}")
        for white, label in ((True, "blancs"), (False, "noirs")):
            ops = collections.defaultdict(collections.Counter)
            for g in f30:
                if g["white"] == white:
                    ops[g.get("opening", "inconnue")][report.outcome(g)] += 1
            top = sorted(ops.items(), key=lambda kv: -sum(kv[1].values()))[:2]
            if top:
                L.append(f"- Ouvertures les plus jouées avec les {label} : "
                         + " ; ".join(f"{n} ({c['victoire']}V/{c['nulle']}N/{c['défaite']}D)" for n, c in top))
    else:
        L.append("- Pas assez de parties de 10 ou 15 min sur 30 jours.")
    L.append("")

    base = focus or f30
    mday = _motifs(base)
    pool = mday if sum(mday.values()) else _motifs(f30)
    axes = []
    for m, _ in pool.most_common(2):
        axes.append((facts.MOTIFS[m].capitalize(), ADVICE[m]))
    miss = [g for g in base if g["result"] != "win" and _max_adv(g) >= 300]
    if miss:
        axes.append(("Conserver un avantage", ADVICE["gain_rate"]))
    L_note = ""
    p_dec = [e for g in base for e in _decisive(g)]
    p_clock = sum(1 for e in p_dec if e.get("clk") is not None and e["clk"] < 60)
    if p_dec and p_clock / len(p_dec) >= 0.25:
        axes.append(("Gestion du temps", "Une bonne part de tes erreurs arrive à moins d'une minute : joue un peu plus vite en début de partie pour garder du temps."))
    elif focus:
        clks = [e["clk"] for g in focus for e in _decisive(g) if e.get("clk") is not None]
        if clks:
            L_note = f"Horloge au moment des erreurs décisives : entre {report.clock(min(clks))} et {report.clock(max(clks))} : le temps n'était pas le problème."
    L += ["## Axes de progression proposés (calculés, à reformuler par le coach)"]
    L += [f"{i}. {title} - {txt}" for i, (title, txt) in enumerate(axes, 1)] or ["- Pas assez de données pour proposer des axes."]
    if focus and not (p_dec and p_clock / len(p_dec) >= 0.25) and L_note:
        L.append(f"- Note : {L_note}")
    L += ["", "## Limites à dire honnêtement",
          f"- Échantillon du jour en rapides 10/15 min : {len(focus)} partie(s)" + (" (trop mince pour parler de tendance ; s'appuyer sur les 30 jours)" if len(focus) < 5 else ""),
          "- Les thèmes sont des étiquettes automatiques, approximatives. Les parties contre des bots et entraîneurs de chess.com ne sont pas comptées.", ""]
    return L
