"""Textes pédagogiques par partie : récit, moments clés, coups réussis. Tout est déduit des données."""
import datetime
import io
import zoneinfo

import chess
import chess.pgn

from coach import facts

TZ = zoneinfo.ZoneInfo("Europe/Zurich")
TC_FR = {"bullet": "bullet", "blitz": "blitz", "rapid": "rapide", "daily": "par correspondance"}
DRAW = {"agreed", "repetition", "stalemate", "insufficient", "50move", "timevsinsufficient"}
LOSS_END = {"checkmated": "par mat", "resigned": "par abandon", "timeout": "au temps", "abandoned": "partie quittée"}
WIN_END = {"checkmated": "par mat", "resigned": "par abandon de l'adversaire",
           "timeout": "au temps (l'adversaire a dépassé son temps)", "abandoned": "l'adversaire a quitté la partie"}
DRAW_END = {"agreed": "par accord", "repetition": "par répétition", "stalemate": "par pat",
            "insufficient": "par matériel insuffisant", "50move": "par la règle des 50 coups",
            "timevsinsufficient": "au temps contre matériel insuffisant"}


def day(g):
    return datetime.datetime.fromtimestamp(g["end"], TZ).date()


def outcome(g):
    return "victoire" if g["result"] == "win" else "nulle" if g["result"] in DRAW else "défaite"


def ending(g):
    if g["result"] == "win":
        return WIN_END.get(g["opp_result"], g["opp_result"])
    if g["result"] in DRAW:
        return DRAW_END.get(g["result"], g["result"])
    return LOSS_END.get(g["result"], g["result"])


def decisive(e, floor=-300):
    return e["loss"] >= 200 and e["eb"] >= floor


def ctrl_fr(ctrl):
    """'600' -> '10 min', '180+2' -> '3 min + 2 s', '1/86400' -> '1 jour par coup'."""
    try:
        if "/" in ctrl:
            n, sec = ctrl.split("/")
            return f"{int(sec) // 86400} jour(s) par coup" if int(n) == 1 else ctrl
        base, _, inc = ctrl.partition("+")
        m = int(base)
        txt = f"{m // 60} min" if m >= 60 and m % 60 == 0 else f"{m} s"
        return txt + (f" + {inc} s" if inc else "")
    except ValueError:
        return ctrl


def clock(sec):
    return "?" if sec is None else f"{sec // 60}:{sec % 60:02d}"


def eval_word(x):
    a = abs(x)
    if a < 60:
        return "à peu près égale"
    side = "pour toi" if x > 0 else "pour l'adversaire"
    if a < 150:
        return f"légèrement meilleure {side}"
    if a < 400:
        return f"nettement meilleure {side}"
    return "gagnante pour toi" if x > 0 else "perdante pour toi"


def sans_of(g):
    game = chess.pgn.read_game(io.StringIO(g["pgn"]))
    b, out = game.board(), []
    for mv in game.mainline_moves():
        out.append(b.san(mv))
        b.push(mv)
    return out


def my_loss(g):
    return {ply: loss for ply, loss, _ in g["my"]}


def gifts(g):
    """Cadeaux de l'adversaire (son coup te fait gagner >= 2 pions) et combien tu en as saisis."""
    me = 1 if g["white"] else -1
    ev, loss = g["ev"], my_loss(g)
    n = len(ev) - 1
    total = taken = 0
    for p in range(1, n + 1):
        if p in loss or me * (ev[p] - ev[p - 1]) < 200 or p == n:
            continue
        total += 1
        if loss.get(p + 1, 999) < 100:
            taken += 1
    return total, taken


def good_moves(g, k=2):
    """Coups où tu as gagné au moins 1,5 pion d'évaluation à toi seul, en jouant presque le meilleur coup."""
    me = 1 if g["white"] else -1
    ev, loss = g["ev"], my_loss(g)
    sans = sans_of(g)
    out = []
    for ply, l in loss.items():
        if l <= 30 and me * (ev[ply] - ev[ply - 1]) >= 150 and ply - 1 < len(sans):
            out.append((me * (ev[ply] - ev[ply - 1]), ply, sans[ply - 1]))
    return [(ply, san) for _, ply, san in sorted(out, reverse=True)[:k]]


def key_errors(g, k=4):
    """Erreurs décisives les plus lourdes, sans la suite immédiate d'une gaffe déjà retenue."""
    es = sorted((e for e in g["errs"] if decisive(e)), key=lambda e: -e["loss"])
    chosen = []
    for e in es:
        if all(abs(e["ply"] - c["ply"]) > 4 for c in chosen):
            chosen.append(e)
        if len(chosen) == k:
            break
    return sorted(chosen, key=lambda e: e["ply"])


def story(g):
    """Récit de la partie sans révéler les coups à étudier (utilisable avant les exercices)."""
    me = 1 if g["white"] else -1
    ev = g["ev"]
    n = len(ev) - 1
    S = []
    head = f"{TC_FR[g['tc']].capitalize()} ({ctrl_fr(g['ctrl'])}), tu jouais les {'blancs' if g['white'] else 'noirs'} contre {g['opp']} ({g['opp_rating']}) : {outcome(g)} {ending(g)}."
    S.append(head)
    if g.get("opening") and g["opening"] != "inconnue":
        S.append(f"Ouverture : {g['opening']}.")
    for coup in (10, 20, 30):
        if n >= 2 * coup + 2:
            S.append(f"Au coup {coup}, la position était {eval_word(me * ev[2 * coup])}.")
    dec = [e for e in g["errs"] if decisive(e)]
    if dec:
        S.append(f"{len(dec)} erreur{'s' if len(dec) > 1 else ''} décisive{'s' if len(dec) > 1 else ''} de ta part (perte d'au moins 2 pions).")
    else:
        S.append("Aucune erreur décisive : partie propre.")
    t, tk = gifts(g)
    if t:
        S.append(f"L'adversaire t'a offert {t} occasion{'s' if t > 1 else ''} d'avantage ; tu en as saisi {tk}.")
    low = [e for e in dec if e["clk"] is not None and e["clk"] < 60]
    clks = [c for _, _, c in g["my"] if c is not None]
    if g["tc"] != "daily" and clks and min(clks) < 30:
        S.append(f"Ton horloge est descendue à {clock(min(clks))}" + (f" ; {len(low)} erreur(s) décisive(s) sous la minute." if low else "."))
    return S


def question_block(i, g, e, title="Position", suffix=""):
    fen = e["fen"]
    tr = facts.trait(fen)
    return [f"### {title} {i}{suffix} : coup {e['n']} d'une partie en {TC_FR[g['tc']]}",
            f"- Partie : {g['url']}",
            f"- Trait aux {tr} : tu joues les {tr}",
            f"- Échiquier : {facts.lichess(fen)}",
            f"- FEN : {fen}",
            f"- Question : {facts.QUESTION}", ""]


def solution_block(i, g, e, title="Position"):
    fen = e["fen"]
    tr = facts.trait(fen)
    deep = e.get("deep")
    best = deep["cands"][0]["uci"] if deep and deep["cands"] else e.get("best_uci")
    pv = deep["cands"][0]["pv_uci"] if deep and deep["cands"] else e.get("pv_uci", [])
    ref = deep["refut_uci"] if deep and deep["refut_uci"] else e.get("refut_uci", [])
    depth = deep["depth"] if deep else e.get("depth", 12)
    w = facts.why_loss(e)
    b1 = chess.Board(fen)
    b1.push(chess.Move.from_uci(e["move_uci"]))
    L = [f"### {title} {i} (corrigé)",
         f"- Partie : {g['url']} - coup {e['n']}, tu jouais les {tr}",
         f"- Ton coup : {facts.say_move(fen, e['move_uci'])}"]
    if best:
        L.append(f"- Meilleur coup : {facts.say_move(fen, best)}")
    L += [f"- Perte mesurée : {e['loss'] / 100:.1f} pion(s) ; évaluation {facts.fmt_eval(e['eb'], e.get('eb_mate'))} avant, "
          f"{facts.fmt_eval(e['ea'], e.get('ea_mate'))} après (profondeur {depth})",
          f"- Pourquoi : {w['phrase']}",
          f"- Thème (étiquette automatique, approximative) : {facts.MOTIFS[w['motif']]}"]
    after = facts.line_facts(b1.fen(), ref, 4)
    if after:
        L.append("- Ce qui se passe après ton coup (ligne du moteur) :")
        L += ["  " + x for x in after]
    good = facts.line_facts(fen, pv, 5)
    if good:
        L.append("- Ligne conseillée par le moteur, coup par coup :")
        L += ["  " + x for x in good]
    if deep:
        for c in deep["cands"][1:]:
            L.append(f"- Autre option solide : {facts.say_move(fen, c['uci'])} (évaluation {facts.fmt_eval(c['cp'], c.get('mate'))})")
    if e.get("clk") is not None and g["tc"] != "daily":
        L.append(f"- Temps restant sur ton horloge : {clock(e['clk'])}" + (" (moins d'une minute)" if e["clk"] < 60 else ""))
    L.append("")
    return L


def game_section(idx, g):
    """Section complète d'une partie pour rapport.md (contient les solutions)."""
    L = [f"## Partie {idx} : {TC_FR[g['tc']]} - {outcome(g)} {ending(g)}", f"- Lien : {g['url']}", ""]
    L += [f"- {s}" for s in story(g)]
    gm = good_moves(g)
    if gm:
        L.append("- Coups réussis : " + " ; ".join(f"coup {(ply + 1) // 2} ({san})" for ply, san in gm))
    L.append("")
    ke = key_errors(g)
    if not ke:
        L += ["Aucun moment clé à corriger dans cette partie.", ""]
    for k, e in enumerate(ke, 1):
        L += solution_block(f"{idx}.{k}", g, e, "Moment clé")
    return L
