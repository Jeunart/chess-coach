import io
import re

import chess
import chess.engine
import chess.pgn

DEPTH = 12
VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
CLK = re.compile(r"\[%clk (\d+):(\d+):(\d+(?:\.\d+)?)\]")


def _phase(n):
    return "ouverture" if n <= 10 else "milieu" if n <= 25 else "finale"


def _tag(before, mv, best, after, reply, me_b, me_a):
    if me_a <= -900 and me_b > -900:
        return "mat_subi"
    if me_b >= 900 and me_a < 900:
        return "mat_rate"
    if reply is not None and after.is_capture(reply) and \
            VAL.get(after.piece_type_at(reply.to_square), 0) >= 3:
        return "piece_en_prise"
    if best is not None and before.is_capture(best) and \
            VAL.get(before.piece_type_at(best.to_square), 0) >= 3:
        return "gain_rate"
    return "autre"


def _evaluate(boards, eng):
    ev, best = [], []
    for b in boards:
        if b.is_game_over():
            if b.is_checkmate():
                ev.append(-1000 if b.turn == chess.WHITE else 1000)
            else:
                ev.append(0)
            best.append(None)
            continue
        info = eng.analyse(b, chess.engine.Limit(depth=DEPTH))
        ev.append(max(-1000, min(1000, info["score"].white().score(mate_score=1000))))
        best.append(info["pv"][0] if info.get("pv") else None)
    return ev, best


def analyze_game(game, eng):
    g = chess.pgn.read_game(io.StringIO(game["pgn"]))
    if g is None:
        return None
    boards, moves, clocks = [g.board()], [], []
    for node in g.mainline():
        m = CLK.search(node.comment or "")
        clocks.append(int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3]) if m else None)
        b = boards[-1].copy()
        b.push(node.move)
        boards.append(b)
        moves.append(node.move)
    ev, best = _evaluate(boards, eng)
    sign = 1 if game["white"] else -1
    errs, mine = [], 0
    for k, mv in enumerate(moves):
        if (k % 2 == 0) != game["white"]:
            continue
        mine += 1
        me_b, me_a = sign * ev[k], sign * ev[k + 1]
        loss = me_b - me_a
        if loss < 100:
            continue
        b = boards[k]
        errs.append({"ply": k + 1, "n": b.fullmove_number, "phase": _phase(b.fullmove_number),
                     "move": b.san(mv), "best": b.san(best[k]) if best[k] else None,
                     "loss": loss, "clk": clocks[k], "fen": b.fen(),
                     "tag": _tag(b, mv, best[k], boards[k + 1], best[k + 1], me_b, me_a)})
    return {"id": game["id"], "end": game["end"], "white": game["white"],
            "rating": game["rating"], "result": game["result"], "moves": mine, "errs": errs}
