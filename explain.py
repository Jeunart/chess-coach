import re

import chess

ART = {chess.PAWN: "le pion", chess.KNIGHT: "le cavalier", chess.BISHOP: "le fou",
       chess.ROOK: "la tour", chess.QUEEN: "la dame", chess.KING: "le roi"}
FEM = {chess.ROOK, chess.QUEEN}
NAMES = {chess.KING: ("Roi", "Rois"), chess.QUEEN: ("Dame", "Dames"), chess.ROOK: ("Tour", "Tours"),
         chess.BISHOP: ("Fou", "Fous"), chess.KNIGHT: ("Cavalier", "Cavaliers"), chess.PAWN: ("Pion", "Pions")}
LEGEND = ("Légende des échiquiers : MAJUSCULES = pièces blanches, minuscules = pièces noires ; "
          "K/k roi, Q/q dame, R/r tour, B/b fou, N/n cavalier, P/p pion ; . = case vide. "
          "Notation des coups : K Roi, Q Dame, R Tour, B Fou, N Cavalier, aucune lettre = pion ; "
          "x = prise ; + = échec ; # = mat ; O-O = petit roque ; O-O-O = grand roque.")


def diagram(fen):
    b = chess.Board(fen)
    white_bottom = b.turn == chess.WHITE
    ranks = range(7, -1, -1) if white_bottom else range(8)
    files = range(8) if white_bottom else range(7, -1, -1)
    rows = []
    for r in ranks:
        cells = [b.piece_at(chess.square(f, r)) for f in files]
        rows.append(f"{r + 1}  " + " ".join(c.symbol() if c else "." for c in cells))
    rows.append("   " + " ".join("abcdefgh"[f] for f in files))
    return "\n".join(rows)


def pieces(fen):
    b = chess.Board(fen)
    out = []
    for color, label in ((chess.WHITE, "Blancs"), (chess.BLACK, "Noirs")):
        parts = []
        for pt in (chess.KING, chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT, chess.PAWN):
            sq = sorted(chess.square_name(s) for s in b.pieces(pt, color))
            if sq:
                parts.append(f"{NAMES[pt][len(sq) > 1]} {' '.join(sq)}")
        out.append(f"{label} : " + ", ".join(parts))
    return "\n".join(out)


def _who(p):
    adj = ("blanche" if p.color else "noire") if p.piece_type in FEM else ("blanc" if p.color else "noir")
    return f"{ART[p.piece_type]} {adj}"


def describe(b, mv):
    p = b.piece_at(mv.from_square)
    if b.is_castling(mv):
        s = "le roi fait le " + ("petit" if chess.square_file(mv.to_square) > 4 else "grand") + " roque"
    else:
        s = f"{_who(p)} va de {chess.square_name(mv.from_square)} en {chess.square_name(mv.to_square)}"
        if b.is_en_passant(mv):
            s += " et prend un pion en passant"
        elif b.is_capture(mv):
            s += f" et prend {_who(b.piece_at(mv.to_square))}"
        if mv.promotion:
            s += f" et devient {ART[mv.promotion].replace('le ', 'un ').replace('la ', 'une ')}"
    c = b.copy()
    c.push(mv)
    return s + (" (échec et mat)" if c.is_checkmate() else " (échec)" if c.is_check() else "")


def speak(fen, sans):
    b = chess.Board(fen)
    out = []
    for i, san in enumerate(sans, 1):
        mv = b.parse_san(san)
        out.append((f"{i}) " if len(sans) > 1 else "") + f"{describe(b, mv)} ({san})")
        b.push(mv)
    return " ".join(out)


def sans_of(variation):
    return re.sub(r"\d+\.(\.\.)?", " ", variation).split()
