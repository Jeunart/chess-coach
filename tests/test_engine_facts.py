import os
import sys

import chess

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from coach import engine, facts  # noqa: E402
from fake_engine import FakeEngine  # noqa: E402


def game(pgn, white, **kw):
    g = {"id": "t1", "url": "https://www.chess.com/game/live/t1", "end": 1793600000, "tc": "blitz",
         "ctrl": "300", "white": white, "rating": 450, "opp_rating": 460, "opp": "x",
         "result": "checkmated", "opp_result": "win", "pgn": pgn}
    g.update(kw)
    return g


SCHOLAR = '[Event "t"]\n\n1. e4 {[%clk 0:05:00]} e5 {[%clk 0:05:00]} 2. Qh5 {[%clk 0:04:58]} Nc6 {[%clk 0:04:50]} 3. Bc4 {[%clk 0:04:55]} Nf6 {[%clk 0:00:20]} 4. Qxf7# 1-0\n'


def test_mat_subi_detecte_avec_horloge():
    rec = engine.analyze_game(game(SCHOLAR, white=False), FakeEngine())
    assert rec["moves"] == 3 and len(rec["ev"]) == 8
    e = rec["errs"][-1]
    assert e["move_uci"] == "g8f6" and e["ea_mate"] == -1 and e["clk"] == 20
    assert facts.why_loss(e)["motif"] == "mat_subi"


def test_gain_rate_prendre_une_piece_gratuite():
    # le cavalier noir en d5 est sans défense, attaqué par la dame ; les blancs jouent a3 au lieu de Dxd5
    pgn = '[SetUp "1"]\n[FEN "6k1/8/8/3n4/8/8/P7/3Q2K1 w - - 0 1"]\n\n1. a3 Nf6 *\n'
    rec = engine.analyze_game(game(pgn, white=True, result="win", opp_result="resigned"), FakeEngine())
    e = rec["errs"][0]
    assert e["best_uci"] == "d1d5" and e["move_uci"] == "a2a3"
    w = facts.why_loss(e)
    assert w["motif"] == "gain_rate" and "cavalier noir en d5" in w["phrase"] and "pas défendu" in w["phrase"]


def test_piece_en_prise_et_reponse_adverse():
    # 1.e4 e5 2.Qh5 Nc6 3.Qxe5?? Nxe5 : la dame blanche est prise
    pgn = '[Event "t"]\n\n1. e4 e5 2. Qh5 Nc6 3. Qxe5 Nxe5 0-1\n'
    rec = engine.analyze_game(game(pgn, white=True, result="resigned", opp_result="win"), FakeEngine())
    e = [x for x in rec["errs"] if x["move_uci"] == "h5e5"][0]
    w = facts.why_loss(e)
    assert w["motif"] == "piece_en_prise" and "dame blanche" in w["phrase"]


def test_lichess_reproduit_le_fen_et_oriente_les_noirs():
    for fen, black in ((chess.STARTING_FEN, False),
                       ("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1", True)):
        url = facts.lichess(fen)
        assert url.startswith("https://lichess.org/analysis/")
        assert url.endswith("?color=black") == black
        assert url.split("analysis/")[1].split("?")[0].replace("_", " ") == fen


def test_fen_invalide_leve_une_erreur():
    try:
        facts.lichess("pas un fen")
    except ValueError:
        return
    raise AssertionError("un FEN invalide doit lever ValueError")


def test_pgn_inutilisable_retourne_none():
    assert engine.analyze_game(game("", white=True), FakeEngine()) is None


def test_deep_stocke_candidats_et_refutation():
    rec = engine.analyze_game(game(SCHOLAR, white=False), FakeEngine(), deep=True)
    d = rec["errs"][-1]["deep"]
    assert d["depth"] == engine.DEEP_DEPTH and d["cands"] and d["refut_uci"][0] == "h5f7"
