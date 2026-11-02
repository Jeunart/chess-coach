import json, re, urllib.request, datetime, collections

USER = "jeunart"
UA = {"User-Agent": "chess-coach-bot (user: jeunart)"}
DRAW = {"agreed", "repetition", "stalemate", "insufficient", "50move", "timevsinsufficient"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def last_games(n=30):
    games = []
    for url in reversed(get(f"https://api.chess.com/pub/player/{USER}/games/archives")["archives"]):
        games = get(url)["games"] + games
        if len(games) >= n * 2:
            break
    games = [g for g in games if g.get("rules") == "chess"]
    games.sort(key=lambda g: g["end_time"])
    return games[-n:]


def side(g):
    if g["white"]["username"].lower() == USER:
        return "blancs", g["white"]
    return "noirs", g["black"]


def issue(r):
    return "V" if r == "win" else "N" if r in DRAW else "D"


def opening(g):
    m = re.search(r'\[ECOUrl "[^"]*/openings/([^"]+)"\]', g.get("pgn", ""))
    return " ".join(m.group(1).split("-")[:3]) if m else "inconnue"


def build(gs):
    col = collections.defaultdict(collections.Counter)
    how = collections.Counter()
    ops = collections.defaultdict(collections.Counter)
    for g in gs:
        c, me = side(g)
        k = issue(me["result"])
        col[c][k] += 1
        if k == "D":
            how[me["result"]] += 1
        ops[(c, opening(g))][k] += 1
    L = [f"# Séance coach - {datetime.date.today()}", "",
         f"## Bilan des {len(gs)} dernières parties de {USER}"]
    L.append(f"Classement: {side(gs[0])[1]['rating']} -> {side(gs[-1])[1]['rating']}")
    for c, n in col.items():
        L.append(f"- {c}: {n['V']} victoires, {n['N']} nulles, {n['D']} défaites")
    pertes = sum(how.values())
    L += ["", f"## Comment je perds ({pertes} défaites)"]
    names = {"checkmated": "mat", "resigned": "abandon", "timeout": "temps écoulé", "abandoned": "partie quittée"}
    for r, n in how.most_common():
        L.append(f"- {names.get(r, r)}: {n}")
    L += ["", "## Ouvertures les plus jouées (V/N/D)"]
    top = sorted(ops.items(), key=lambda kv: -sum(kv[1].values()))[:6]
    for (c, o), n in top:
        L.append(f"- {c}, {o}: {n['V']}/{n['N']}/{n['D']}")
    L += ["", "## Focus de la séance",
          "Avant chaque coup: 1) Quelle pièce adverse menace quoi ? 2) Est-ce que ma pièce jouée est protégée ?",
          "", "## Règle pour le coach",
          "Ne calcule aucune variante toi-même. Pose une question à la fois et attends ma réponse."]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    open("seance.md", "w", encoding="utf-8").write(build(last_games(30)))
