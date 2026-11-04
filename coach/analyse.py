"""Import chess.com + analyse Stockfish incrémentale. Écrit data/v2/games.jsonl et manifest.json.

python -m coach.analyse
"""
import datetime
import json
import multiprocessing as mp
import os
import sys

import chess.engine

from coach import chesscom, engine, report

PATH = "data/v2/games.jsonl"
MANIFEST = "data/v2/manifest.json"
STOCKFISH = os.environ.get("STOCKFISH", "/usr/games/stockfish")
DEEP_DAYS = int(os.environ.get("DEEP_DAYS", "3"))
_eng = None


def _work(args):
    global _eng
    game, deep = args
    if _eng is None:
        _eng = chess.engine.SimpleEngine.popen_uci(STOCKFISH)
        _eng.configure({"Threads": 1, "Hash": 64})
    try:
        return game["id"], engine.analyze_game(game, _eng, deep=deep)
    except Exception as e:  # noqa: BLE001
        print("échec", game["id"], e, file=sys.stderr)
        return game["id"], None


def main():
    os.makedirs("data/v2", exist_ok=True)
    done = set()
    if os.path.exists(PATH):
        done = {json.loads(l)["id"] for l in open(PATH, encoding="utf-8") if l.strip()}
    new, manifest = chesscom.all_games(skip_ids=done)
    now = datetime.datetime.now(report.TZ)
    today = str(now.date())
    limit_ts = now.timestamp() - DEEP_DAYS * 86400
    work = []
    for g in new:
        g["seen"] = today
        work.append((g, g["end"] >= limit_ts))
    print(len(done), "déjà analysées ;", len(work), "à analyser")
    failed = []
    with mp.Pool(mp.cpu_count()) as pool, open(PATH, "a", encoding="utf-8") as out:
        for gid, rec in pool.imap(_work, work):
            if rec is None:
                failed.append(gid)
                continue
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush()
    ids = {json.loads(l)["id"] for l in open(PATH, encoding="utf-8") if l.strip()} if os.path.exists(PATH) else set()
    total = sum(manifest["total"].values())
    manifest.update({"genere": now.isoformat(timespec="seconds"), "analysees": len(ids), "echecs": failed,
                     "manquantes": total - len(ids)})
    json.dump(manifest, open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("manifeste :", manifest)
    if total - len(ids) > len(failed):
        print("⚠ des parties importables ne sont pas analysées", file=sys.stderr)


if __name__ == "__main__":
    main()
