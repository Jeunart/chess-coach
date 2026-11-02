import json
import multiprocessing as mp
import os
import sys

import chess.engine

import chesscom
import engine

PATH = "data/a3.jsonl"
STOCKFISH = os.environ.get("STOCKFISH", "/usr/games/stockfish")
LIMIT = int(os.environ.get("LIMIT", "1500"))
_eng = None


def _work(game):
    global _eng
    if _eng is None:
        _eng = chess.engine.SimpleEngine.popen_uci(STOCKFISH)
        _eng.configure({"Threads": 1, "Hash": 64})
    try:
        return engine.analyze_game(game, _eng)
    except Exception as e:
        print("echec", game["id"], e, file=sys.stderr)
        return None


def main():
    done = set()
    if os.path.exists(PATH):
        done = {json.loads(l)["id"] for l in open(PATH, encoding="utf-8") if l.strip()}
    todo = chesscom.rapid_games(skip_ids=done)[:LIMIT]
    print(len(done), "deja analysees ;", len(todo), "a analyser")
    os.makedirs("data", exist_ok=True)
    with mp.Pool(mp.cpu_count()) as pool, open(PATH, "a", encoding="utf-8") as out:
        for res in pool.imap(_work, todo):
            if res:
                out.write(json.dumps(res, ensure_ascii=False) + "\n")
                out.flush()


if __name__ == "__main__":
    main()
