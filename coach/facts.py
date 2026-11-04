"""Faits vérifiés sur les positions, calculés par python-chess.

Rien ici n'est deviné par un LLM : le professeur (ChatGPT) ne fait que mettre en mots
ces faits et les lignes de Stockfish.
"""
import chess

import explain

VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 100}

MOTIFS = {
    "piece_en_prise": "pièce laissée en prise",
    "menace_ignoree": "menace adverse ignorée",
    "fourchette_subie": "fourchette subie",
    "mat_subi": "mat subi",
    "mat_rate": "mat manqué",
    "gain_rate": "gain de matériel manqué",
    "autre": "erreur positionnelle",
}

# Questions posées à l'élève AVANT de révéler la solution (elles ne dévoilent pas le motif).
QUESTION = ("Avant de jouer : quels sont les échecs, les prises et les menaces possibles, "
            "pour toi comme pour l'adversaire ? Puis dis-moi ton coup.")


def lichess(fen):
    """Lien Lichess (échiquier cliquable) reproduisant exactement le FEN, côté du joueur au trait."""
    b = chess.Board(fen)
    url = "https://lichess.org/analysis/" + b.fen().replace(" ", "_")
    return url + ("?color=black" if b.turn == chess.BLACK else "")


def trait(fen):
    return "blancs" if chess.Board(fen).turn == chess.WHITE else "noirs"


def fmt_eval(cp, mate=None):
    if mate is not None and mate != 0:
        who = "toi" if mate > 0 else "l'adversaire"
        return f"mat en {abs(mate)} pour {who}"
    return f"{cp / 100:+.1f}"


def legal_line(fen, ucis):
    """[(plateau avant le coup, coup)] ; s'arrête à la première incohérence."""
    b = chess.Board(fen)
    out = []
    for u in ucis:
        try:
            mv = chess.Move.from_uci(u)
        except ValueError:
            break
        if mv not in b.legal_moves:
            break
        out.append((b.copy(), mv))
        b.push(mv)
    return out


def san_of(fen, uci):
    b = chess.Board(fen)
    return b.san(chess.Move.from_uci(uci))


def say_move(fen, uci):
    b = chess.Board(fen)
    mv = chess.Move.from_uci(uci)
    return f"{explain.describe(b, mv)} ({b.san(mv)})"


def san_line(fen, ucis, limit=6):
    steps = legal_line(fen, ucis[:limit])
    if not steps:
        return ""
    b0, _ = steps[0]
    return b0.variation_san([m for _, m in steps])


def who_sq(b, sq):
    return f"{explain._who(b.piece_at(sq))} en {chess.square_name(sq)}"


def _fem(b, sq):
    return "e" if b.piece_at(sq).piece_type in explain.FEM else ""


def hanging(b, color, min_value=3):
    """Pièces de `color` (hors roi et pions) attaquées et soit non défendues, soit attaquées
    par une pièce de moindre valeur. Retourne [(case, 'sans_defense'|'moindre_valeur')]."""
    out = []
    for sq, p in b.piece_map().items():
        if p.color != color or p.piece_type == chess.KING or VAL[p.piece_type] < min_value:
            continue
        att = b.attackers(not color, sq)
        if not att:
            continue
        if not b.attackers(color, sq):
            out.append((sq, "sans_defense"))
        elif min(VAL[b.piece_type_at(a)] for a in att) < VAL[p.piece_type]:
            out.append((sq, "moindre_valeur"))
    return out


def hanging_phrase(b, sq, kind):
    f = _fem(b, sq)
    base = f"{who_sq(b, sq)} est attaqué{f}"
    return base + (f" et n'est pas défendu{f}" if kind == "sans_defense" else " par une pièce de moindre valeur")


def line_facts(fen, ucis, limit=5):
    """Une ligne par coup : description en mots, gain de matériel, pièces menacées ensuite."""
    out = []
    for i, (b, mv) in enumerate(legal_line(fen, ucis[:limit]), 1):
        mover = b.turn
        cap = b.piece_at(mv.to_square) if b.is_capture(mv) else None
        text = f"{explain.describe(b, mv)} ({b.san(mv)})"
        after = b.copy()
        after.push(mv)
        extra = []
        if cap:
            extra.append(f"prise {de(explain._who(cap))}")
        extra += [hanging_phrase(after, s, k) for s, k in hanging(after, not mover)]
        out.append(f"{i}. {text}" + (" - " + " ; ".join(extra) if extra else ""))
    return out


def de(who):
    """'le pion noir' -> 'du pion noir', 'la dame' -> 'de la dame', "l'..." -> "de l'..." """
    if who.startswith("le "):
        return "du " + who[3:]
    if who.startswith("la "):
        return "de la " + who[3:]
    return "de " + who


def _plural(n, word="coup"):
    return f"{n} {word}{'s' if n > 1 else ''}"


def why_loss(e):
    """Explique une erreur. `e` : entrée d'erreur du schéma v2. Retourne {motif, phrase, details}."""
    b0 = chess.Board(e["fen"])
    me = b0.turn
    mv = chess.Move.from_uci(e["move_uci"])
    best = chess.Move.from_uci(e["best_uci"]) if e.get("best_uci") else None
    b1 = b0.copy()
    b1.push(mv)
    ea_mate, eb_mate = e.get("ea_mate"), e.get("eb_mate")
    details = []

    if ea_mate is not None and ea_mate < 0 and not (eb_mate is not None and eb_mate < 0):
        return {"motif": "mat_subi", "details": details,
                "phrase": f"Après ton coup, l'adversaire avait un mat en {_plural(-ea_mate)}."}
    if eb_mate is not None and eb_mate > 0 and not (ea_mate is not None and ea_mate > 0):
        return {"motif": "mat_rate", "details": details,
                "phrase": f"Tu avais un mat en {_plural(eb_mate)} et ton coup l'a laissé passer."}

    # gain gratuit manqué : le meilleur coup prend une pièce menacée ou mal défendue
    if best and b0.is_capture(best) and best != mv:
        target = b0.piece_at(best.to_square)
        if target and VAL[target.piece_type] >= 3 and best.to_square in dict(hanging(b0, not me)):
            kind = dict(hanging(b0, not me))[best.to_square]
            fem = _fem(b0, best.to_square)
            il, obj = ("elle", "la") if fem else ("il", "le")
            how = f"{il} n'était pas défendu{fem}" if kind == "sans_defense" else f"tu {obj} prenais avec une pièce de moindre valeur"
            return {"motif": "gain_rate", "details": details,
                    "phrase": f"Tu pouvais gagner {who_sq(b0, best.to_square)} : {how}."}

    ref = legal_line(b1.fen(), e.get("refut_uci", []))
    still = {s for s, _ in hanging(b0, me)} & {s for s, _ in hanging(b1, me)}
    still.discard(mv.from_square)
    if ref:
        rb, rmv = ref[0]
        cap = rb.piece_at(rmv.to_square) if rb.is_capture(rmv) else None
        if cap and cap.color == me and VAL[cap.piece_type] >= 3:
            if rmv.to_square in still:
                return {"motif": "menace_ignoree", "details": details,
                        "phrase": (f"L'adversaire menaçait {who_sq(b0, rmv.to_square)} et ton coup n'a pas réglé "
                                   f"cette menace : il la prend avec {rb.san(rmv)}.")}
            hang = dict(hanging(b1, me)).get(rmv.to_square)
            moved = rmv.to_square == mv.to_square
            if hang == "sans_defense":
                where = "la pièce que tu viens de déplacer" if moved else "une pièce restée sans défense"
                phrase = f"Après ton coup, {where} ({who_sq(b1, rmv.to_square)}) n'était pas défendu{_fem(b1, rmv.to_square)} : l'adversaire la prend avec {rb.san(rmv)}."
            else:
                phrase = (f"Après ton coup, l'adversaire gagne {who_sq(b1, rmv.to_square)} avec {rb.san(rmv)} "
                          f"(échange défavorable pour toi).")
            return {"motif": "piece_en_prise", "details": details, "phrase": phrase}
        # fourchette : la pièce adverse attaque ensuite au moins deux de tes pièces importantes
        ra = rb.copy()
        ra.push(rmv)
        mover_piece = ra.piece_at(rmv.to_square)
        targets = [s for s in ra.attacks(rmv.to_square)
                   if ra.piece_at(s) and ra.piece_at(s).color == me and ra.piece_at(s).piece_type != chess.PAWN
                   and (VAL[ra.piece_at(s).piece_type] >= VAL[mover_piece.piece_type] or not ra.attackers(me, s))]
        if len(targets) >= 2 and mover_piece.piece_type != chess.KING:
            names = " et ".join(who_sq(ra, s) for s in targets[:2])
            return {"motif": "fourchette_subie", "details": details,
                    "phrase": f"Le coup adverse {rb.san(rmv)} attaque en même temps {names} : c'est une fourchette."}

    if still:
        s = sorted(still)[0]
        return {"motif": "menace_ignoree", "details": details,
                "phrase": f"{who_sq(b0, s)} était menacé{_fem(b0, s)} avant ton coup et l'est resté{_fem(b0, s)}."}

    for i, (rb, rm) in enumerate(ref[:4]):
        if i % 2:
            continue  # coups adverses seulement
        ra = rb.copy()
        ra.push(rm)
        h = hanging(ra, me)
        if h:
            sq, kind = h[0]
            return {"motif": "autre", "details": details,
                    "phrase": (f"Pas de gain immédiat pour l'adversaire, mais après {rb.san(rm)} (dans la suite du moteur) "
                               f"{hanging_phrase(ra, sq, kind)} : ton coup te fait perdre du temps et de l'initiative.")}

    hints = []
    if best:
        if b0.is_castling(best):
            hints.append("le meilleur coup était de roquer pour mettre ton roi à l'abri")
        elif b0.gives_check(best):
            hints.append("le meilleur coup donnait échec")
        elif b0.is_capture(best):
            hints.append("le meilleur coup était une prise")
    phrase = ("Pas de tactique immédiate : ton coup a surtout dégradé ta position"
              + (" ; " + hints[0] if hints else "") + ".")
    return {"motif": "autre", "details": details, "phrase": phrase}
