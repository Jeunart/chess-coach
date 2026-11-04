"""Import exhaustif des parties chess.com (bullet, blitz, rapid, daily ; échecs standard)."""
import collections
import json
import time
import urllib.request

USER = "jeunart"
UA = {"User-Agent": "chess-coach-bot (user: jeunart)"}
CLASSES = ("bullet", "blitz", "rapid", "daily")


def _get(url, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 - on réessaie puis on échoue bruyamment
            last = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"API chess.com injoignable : {url} ({last})")


def convert(g):
    """Partie de l'API -> enregistrement minimal ; None si hors périmètre."""
    if g.get("rules") != "chess" or g.get("time_class") not in CLASSES:
        return None
    white = g["white"]["username"].lower() == USER
    me, opp = (g["white"], g["black"]) if white else (g["black"], g["white"])
    return {"id": g["url"].rstrip("/").split("/")[-1], "url": g["url"], "end": g["end_time"],
            "tc": g["time_class"], "ctrl": g.get("time_control", ""), "white": white,
            "rating": me["rating"], "opp_rating": opp["rating"], "opp": opp["username"],
            "result": me["result"], "opp_result": opp["result"], "pgn": g.get("pgn", "")}


def all_games(skip_ids=()):
    """(nouvelles parties triées, manifeste). Lève une erreur si une archive est injoignable :
    on ne publie jamais un import partiel comme s'il était complet."""
    archives = _get(f"https://api.chess.com/pub/player/{USER}/games/archives")["archives"]
    new, total, excluded = [], collections.Counter(), collections.Counter()
    for url in archives:
        for g in _get(url).get("games", []):
            rec = convert(g)
            if rec is None:
                excluded[f"{g.get('rules')}/{g.get('time_class')}"] += 1
                continue
            total[rec["tc"]] += 1
            if rec["id"] not in skip_ids:
                new.append(rec)
    new.sort(key=lambda r: r["end"])
    return new, {"archives": len(archives), "total": dict(total), "exclues": dict(excluded)}
