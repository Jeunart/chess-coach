import json
import urllib.request

USER = "jeunart"
UA = {"User-Agent": "chess-coach-bot (user: jeunart)"}


def _get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def rapid_games(skip_ids=()):
    """Parties rapides classiques, de la plus ancienne a la plus recente."""
    out = []
    for url in _get(f"https://api.chess.com/pub/player/{USER}/games/archives")["archives"]:
        for g in _get(url)["games"]:
            if g.get("rules") != "chess" or g.get("time_class") != "rapid":
                continue
            gid = g["url"].rstrip("/").split("/")[-1]
            if gid in skip_ids:
                continue
            white = g["white"]["username"].lower() == USER
            me = g["white"] if white else g["black"]
            out.append({"id": gid, "end": g["end_time"], "white": white,
                        "rating": me["rating"], "result": me["result"],
                        "pgn": g.get("pgn", "")})
    out.sort(key=lambda x: x["end"])
    return out
