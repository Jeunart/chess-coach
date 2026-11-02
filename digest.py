import datetime
import json
import os
import zoneinfo

import explain
import picks

TZ = zoneinfo.ZoneInfo("Europe/Zurich")
LINK = "https://www.chess.com/game/live/"
FENCE = chr(96) * 3
LEGEND_NOTE = "Pour chaque position : montre l'échiquier tel quel, puis pose la question ; les coups sont décrits en mots avant la notation."
THEME = {
    "piece_en_prise": "Avant chaque coup : la pièce que je déplace est-elle protégée ? Une autre pièce reste-t-elle sans défense ?",
    "mat_subi": "Sécurité du roi : avant chaque coup, chercher les échecs et les mats adverses en 1 ou 2 coups.",
    "gain_rate": "Chercher d'abord les captures et les échecs : y a-t-il une pièce adverse gratuite ?",
    "mat_rate": "Chercher les échecs forcés : un mat en 1 ou 2 coups existe-t-il pour moi ?",
    "autre": "Se demander à chaque coup : que menace mon adversaire, et mon coup y répond-il ?",
}


def load(path="data/a3.jsonl"):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def day(g):
    return datetime.datetime.fromtimestamp(g["end"], TZ).date()


def verdict(g):
    r = g["result"]
    return "gagnée" if r == "win" else "nulle" if r in picks.DRAW else "perdue"


def block(title, g, e, tag=True):
    fen = e["fen"]
    trait = "blancs" if fen.split()[1] == "w" else "noirs"
    L = [f"### {title} : {LINK}{g['id']} coup {e['n']}, trait aux {trait} ({trait} en bas de l'échiquier)",
         FENCE, explain.diagram(fen), FENCE, explain.pieces(fen), f"FEN : {fen}",
         "À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :",
         f"- Mon coup : {explain.speak(fen, [e['move']])}"]
    sans = explain.sans_of(e["pv"]) if e.get("pv") else ([e["best"]] if e["best"] else [])
    L.append(f"- Ligne du moteur (meilleur coup en premier) : {explain.speak(fen, sans)}")
    L.append(f"- Perte : {e['loss'] / 100:.1f} pions" + (f" ; type d'erreur : {picks.TAGS[e['tag']]}" if tag else ""))
    return "\n".join(L) + "\n"


def stats(gs):
    n = max(len(gs), 1)
    return sum(g["result"] == "win" for g in gs), sum(len(picks.decisive(g)) for g in gs) / n


def build(games, today=None):
    today = today or datetime.datetime.now(TZ).date()
    last, prev = games[-30:], games[-60:-30]
    w, b = stats(last)
    L = [f"# Séance coach - {today}", "", "## Bilan (30 dernières parties rapides)",
         f"- Classement : {last[0]['rating']} -> {last[-1]['rating']} ; victoires : {w}/{len(last)}",
         f"- Bourdes décisives par partie : {b:.1f}"
         + (f" (30 parties précédentes : {stats(prev)[1]:.1f})" if prev else "")]
    weak = picks.weakness(last)
    d = today - datetime.timedelta(days=1)
    dg = [g for g in games if day(g) == d] or [g for g in games if day(g) == day(games[-1])]
    L += ["", f"## Parties du {day(dg[0])} (revue)"]
    L += [f"- {LINK}{g['id']} : {'blancs' if g['white'] else 'noirs'}, {verdict(g)}, "
          f"{len(picks.decisive(g))} bourdes décisives" for g in dg]
    L += ["Moments critiques (position jouable où j'ai perdu l'avantage) :"]
    L += [LEGEND_NOTE, explain.LEGEND, ""]
    L += [block(f"Moment {k}", g, e) for k, (g, e) in enumerate(picks.moments(dg, total=4), 1)] or ["- aucun moment critique net"]
    L += ["", "## Puzzles tirés de mes anciennes bourdes (solution après ma réponse)"]
    L += [block(f"Puzzle {k}", g, e, False) for k, (g, e) in
          enumerate(picks.puzzles(games, {g["id"] for g in dg}, weak, today, k=3), 1)]
    L += ["", f"## Focus et mini-cours : {picks.TAGS[weak]}", THEME[weak]]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    s = build(load())
    os.makedirs("seances", exist_ok=True)
    for p in ("seance.md", f"seances/{datetime.datetime.now(TZ).date()}.md"):
        open(p, "w", encoding="utf-8").write(s)
