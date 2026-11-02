import collections
import datetime
import random

TAGS = {"mat_subi": "mat subi", "mat_rate": "mat manqué", "piece_en_prise": "pièce laissée en prise",
        "gain_rate": "gain de pièce manqué", "autre": "autre erreur"}
DRAW = {"agreed", "repetition", "stalemate", "insufficient", "50move", "timevsinsufficient"}


def decisive(g, floor=-300):
    """Bourdes (perte >= 2 pions) jouées alors que la position n'était pas déjà perdue."""
    return [e for e in g["errs"] if e["loss"] >= 200 and e.get("eb", 0) >= floor]


def weakness(games):
    c = collections.Counter(e["tag"] for g in games for e in decisive(g) if e["tag"] != "autre")
    return c.most_common(1)[0][0] if c else "autre"


def moments(day_games, per_game=2, total=6):
    out = []
    for g in day_games:
        es = [e for e in decisive(g, -150)]
        if not es:
            continue
        picks = [es[0]] + sorted(es[1:], key=lambda e: -e["loss"])[:per_game - 1]
        out += [(g, e) for e in picks]
    return out[:total]


def puzzles(games, exclude_ids, weak, today, k=5):
    pool = [(g, e) for g in games if g["id"] not in exclude_ids for e in g["errs"]
            if e["loss"] >= 300 and e.get("eb", 0) >= -100 and e["best"]]
    rnd = random.Random(str(today))
    pref = [p for p in pool if p[1]["tag"] == weak]
    picks = rnd.sample(pref, min(3, len(pref)))
    rest = [p for p in pool if p not in picks]
    return picks + rnd.sample(rest, min(k - len(picks), len(rest)))
