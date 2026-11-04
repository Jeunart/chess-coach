import re


def name(pgn):
    """Nom lisible de l'ouverture d'après l'URL ECO du PGN chess.com ; 'inconnue' sinon."""
    m = re.search(r'\[ECOUrl "[^"]*/openings/([^"]+)"\]', pgn or "")
    if not m:
        return "inconnue"
    parts = []
    for seg in m.group(1).split("-"):
        if re.search(r"\d|\.\.\.", seg):
            break
        parts.append(seg)
    return " ".join(parts[:5]) or "inconnue"
