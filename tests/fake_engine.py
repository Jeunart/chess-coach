"""Moteur factice pour les tests : matériel + mat en 1, profondeur 2. Même interface que Stockfish."""
import chess
import chess.engine

PV = {chess.PAWN: 100, chess.KNIGHT: 300, chess.BISHOP: 300, chess.ROOK: 500, chess.QUEEN: 900}
MATE = 100000


def _material(b):
    s = 0
    for p in b.piece_map().values():
        v = PV.get(p.piece_type, 0)
        s += v if p.color == b.turn else -v
    return s  # du point de vue du camp au trait


def _value(b, depth):
    if b.is_checkmate():
        return -MATE
    if b.is_stalemate() or b.is_insufficient_material():
        return 0
    if depth == 0:
        return _material(b)
    best = -MATE * 2
    for m in b.legal_moves:
        b.push(m)
        best = max(best, -_value(b, depth - 1))
        b.pop()
    return best


class FakeEngine:
    def analyse(self, board, limit, multipv=None):
        scored = []
        for m in board.legal_moves:
            board.push(m)
            v = -_value(board, 1)
            reply = next(iter(board.legal_moves), None) if not board.is_game_over() else None
            best_reply, rv = None, None
            for r in board.legal_moves:
                board.push(r)
                x = -_value(board, 0) if not board.is_checkmate() else -MATE
                board.pop()
                if rv is None or x < rv:  # l'adversaire minimise notre valeur ; x est de son point de vue
                    pass
            board.pop()
            scored.append((v, m))
        scored.sort(key=lambda t: -t[0])

        def pack(v, m):
            if v >= MATE - 10:
                sc = chess.engine.Mate(1)
            elif v <= -MATE + 10:
                sc = chess.engine.Mate(-1)
            else:
                sc = chess.engine.Cp(v)
            b2 = board.copy()
            b2.push(m)
            pv = [m]
            if not b2.is_game_over():
                bestr = max(b2.legal_moves, key=lambda r: self_val(b2, r))
                pv.append(bestr)
            return {"score": chess.engine.PovScore(sc, board.turn), "pv": pv, "depth": limit.depth}

        def self_val(b2, r):
            b2.push(r)
            v = -_value(b2, 0) if not b2.is_checkmate() else MATE
            b2.pop()
            return v

        if multipv:
            return [pack(v, m) for v, m in scored[:multipv]]
        return pack(*scored[0])
