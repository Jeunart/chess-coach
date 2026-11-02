import datetime
import json
import zoneinfo

import picks

TZ = zoneinfo.ZoneInfo("Europe/Zurich")
LINK = "https://www.chess.com/game/live/"
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


def line(g, e, tag=True):
    trait = "blancs" if e["fen"].split()[1] == "w" else "noirs"
    s = (f"- {LINK}{g['id']} coup {e['n']}, trait aux {trait}. FEN: {e['fen']} | Mon coup: {e['move']} | "
         f"Ligne du moteur, meilleur coup en premier (à révéler APRÈS ma réponse): {e.get('pv') or e['best']} | Perte: {e['loss'] / 100:.1f} pions")
    return s + (f" | Type: {picks.TAGS[e['tag']]}" if tag else "")


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
    L += [line(g, e) for g, e in picks.moments(dg)] or ["- aucun moment critique net"]
    L += ["", "## Puzzles tirés de mes anciennes bourdes (solution après ma réponse)"]
    L += [line(g, e, False) for g, e in picks.puzzles(games, {g["id"] for g in dg}, weak, today)]
    L += ["", f"## Focus et mini-cours : {picks.TAGS[weak]}", THEME[weak]]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    open("seance.md", "w", encoding="utf-8").write(build(load()))
