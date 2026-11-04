"""Diagnostic d'import : compare les compteurs officiels chess.com (stats du profil) au contenu des archives.

python -m coach.diagnostic   (lecture seule, ne modifie aucun fichier du dépôt)
"""
import collections

from coach import chesscom

U = chesscom.USER
BASE = f"https://api.chess.com/pub/player/{U}"


def main():
    stats = chesscom._get(f"{BASE}/stats")
    print("=== Compteurs officiels (stats du profil : victoires + défaites + nulles)")
    off_total = 0
    for k, v in sorted(stats.items()):
        rec = v.get("record") if isinstance(v, dict) else None
        if rec:
            n = rec.get("win", 0) + rec.get("loss", 0) + rec.get("draw", 0)
            off_total += n
            print(f"  {k:20s} {n:5d}  (V {rec.get('win', 0)} / D {rec.get('loss', 0)} / N {rec.get('draw', 0)})")
    print(f"  TOTAL officiel       {off_total:5d}")

    archives = chesscom._get(f"{BASE}/games/archives")["archives"]
    print(f"\n=== Archives : {len(archives)} mois ({archives[0].split('/games/')[1]} -> {archives[-1].split('/games/')[1]})")
    by = collections.Counter()
    per_month = {}
    ids = collections.Counter()
    no_pgn = 0
    results = collections.Counter()
    for url in archives:
        games = chesscom._get(url).get("games", [])
        per_month[url.split("/games/")[1]] = len(games)
        for g in games:
            by[(g.get("rules"), g.get("time_class"))] += 1
            ids[g["url"]] += 1
            no_pgn += 0 if g.get("pgn") else 1
            me = g["white"] if g["white"]["username"].lower() == U else g["black"]
            results[me["result"]] += 1
    for k, n in sorted(by.items(), key=lambda kv: -kv[1]):
        print(f"  rules={k[0]!s:10s} classe={k[1]!s:8s} {n:5d}")
    print(f"  TOTAL archives       {sum(by.values()):5d} ; urls uniques {len(ids)} ; doublons {sum(1 for c in ids.values() if c > 1)} ; sans PGN {no_pgn}")
    print("  par mois :", dict(per_month))
    print("  résultats :", dict(results))
    print(f"\n=== Écart officiel - archives : {off_total - sum(by.values())}")
    prof = chesscom._get(BASE)
    print("profil :", {k: prof.get(k) for k in ("joined", "last_online", "status")})


if __name__ == "__main__":
    main()
