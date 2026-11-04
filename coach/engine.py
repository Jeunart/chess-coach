"""Analyse Stockfish, schéma v2.

Passe 1 (profondeur 12) sur tous les coups ; passe 2 approfondie (profondeur 18, MultiPV 3,
et réfutation du coup joué) sur les erreurs décisives des parties récentes.
Les variantes sont conservées en UCI ; la conversion en SAN et en mots se fait à l'affichage.
"""
import io
import re

import chess
import chess.engine
import chess.pgn

import opening

DEPTH = 12
DEEP_DEPTH = 18
DEEP_REFUT_DEPTH = 16
PV_LEN = 8
DECISIVE_LOSS = 200
FLOOR = -300
CLK = re.compile(r"\[%clk (\d+):(\d+):(\d+(?:\.\d+)?)\]")


def phase(n):
    return "ouverture" if n <= 10 else "milieu" if n <= 25 else "finale"


def _clamp(cp):
    return max(-1000, min(1000, cp))


def _evaluate(boards, eng):
    ev, mates, pvs = [], [], []
    for b in boards:
        if b.is_game_over():
            ev.append((-1000 if b.turn == chess.WHITE else 1000) if b.is_checkmate() else 0)
            mates.append(None)
            pvs.append([])
            continue
        info = eng.analyse(b, chess.engine.Limit(depth=DEPTH))
        sc = info["score"].white()
        ev.append(_clamp(sc.score(mate_score=1000)))
        mates.append(sc.mate())
        pvs.append(list(info.get("pv", []))[:PV_LEN])
    return ev, mates, pvs


def _deep(b0, b1, eng, me):
    cands = []
    for info in eng.analyse(b0, chess.engine.Limit(depth=DEEP_DEPTH), multipv=3):
        pv = list(info.get("pv", []))[:PV_LEN]
        if not pv:
            continue
        sc = info["score"].pov(me)
        cands.append({"uci": pv[0].uci(), "cp": _clamp(sc.score(mate_score=1000)), "mate": sc.mate(),
                      "pv_uci": [m.uci() for m in pv]})
    refut = []
    if not b1.is_game_over():
        info = eng.analyse(b1, chess.engine.Limit(depth=DEEP_REFUT_DEPTH))
        refut = [m.uci() for m in list(info.get("pv", []))[:PV_LEN]]
    return {"depth": DEEP_DEPTH, "cands": cands, "refut_uci": refut}


def analyze_game(game, eng, deep=False):
    """Retourne l'enregistrement v2 ou None si le PGN est inutilisable."""
    g = chess.pgn.read_game(io.StringIO(game["pgn"]))
    if g is None or not list(g.mainline_moves()):
        return None
    boards, moves, clocks = [g.board()], [], []
    for node in g.mainline():
        m = CLK.search(node.comment or "")
        clocks.append(int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3]) if m else None)
        b = boards[-1].copy()
        b.push(node.move)
        boards.append(b)
        moves.append(node.move)
    ev, mates, pvs = _evaluate(boards, eng)
    sign = 1 if game["white"] else -1
    me_color = chess.WHITE if game["white"] else chess.BLACK
    errs, my = [], []
    for k, mv in enumerate(moves):
        if (k % 2 == 0) != game["white"]:
            continue
        me_b, me_a = sign * ev[k], sign * ev[k + 1]
        loss = me_b - me_a
        clk = None if clocks[k] is None else int(clocks[k])
        my.append([k + 1, loss, clk])
        if loss < 100:
            continue
        b = boards[k]
        e = {"ply": k + 1, "n": b.fullmove_number, "phase": phase(b.fullmove_number),
             "fen": b.fen(), "move_uci": mv.uci(),
             "best_uci": pvs[k][0].uci() if pvs[k] else None,
             "pv_uci": [m.uci() for m in pvs[k]], "refut_uci": [m.uci() for m in pvs[k + 1]],
             "loss": loss, "eb": me_b, "ea": me_a, "clk": clk, "depth": DEPTH,
             "eb_mate": None if mates[k] is None else sign * mates[k],
             "ea_mate": None if mates[k + 1] is None else sign * mates[k + 1]}
        if deep and loss >= DECISIVE_LOSS and me_b >= FLOOR:
            e["deep"] = _deep(b, boards[k + 1], eng, me_color)
        errs.append(e)
    return {"id": game["id"], "url": game["url"], "end": game["end"], "tc": game["tc"], "ctrl": game["ctrl"],
            "white": game["white"], "rating": game["rating"], "opp_rating": game["opp_rating"],
            "opp": game["opp"], "result": game["result"], "opp_result": game["opp_result"],
            "opening": opening.name(game["pgn"]), "moves": len(my), "ev": ev, "my": my, "errs": errs,
            "deep": bool(deep), "pgn": game["pgn"], "seen": game.get("seen")}
