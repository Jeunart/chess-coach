import datetime
import json
import os
import re
import sys

import chess

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from coach import engine, render, report  # noqa: E402
from fake_engine import FakeEngine  # noqa: E402

TODAY = datetime.date(2026, 11, 4)
SCHOLAR = '[Event "t"]\n[ECOUrl "https://www.chess.com/openings/Bishops-Opening-Berlin-Defense-3.Bc4"]\n\n1. e4 {[%clk 0:05:00]} e5 {[%clk 0:05:00]} 2. Qh5 {[%clk 0:04:58]} Nc6 {[%clk 0:04:50]} 3. Bc4 {[%clk 0:04:55]} Nf6 {[%clk 0:00:20]} 4. Qxf7# 1-0\n'
FREE = '[SetUp "1"]\n[FEN "6k1/8/8/3n4/8/8/P7/3Q2K1 w - - 0 1"]\n\n1. a3 Nf6 2. Qd8+ Ne8 *\n'
QUEEN = '[Event "t"]\n\n1. e4 e5 2. Qh5 Nc6 3. Qxe5 Nxe5 0-1\n'


def ts(d, hour=12):
    return datetime.datetime(d.year, d.month, d.day, hour, tzinfo=report.TZ).timestamp()


def make(gid, pgn, white, d, result, opp_result, tc="blitz"):
    g = {"id": gid, "url": f"https://www.chess.com/game/live/{gid}", "end": ts(d), "tc": tc, "ctrl": "300",
         "white": white, "rating": 450, "opp_rating": 460, "opp": "adv", "result": result,
         "opp_result": opp_result, "pgn": pgn, "seen": str(TODAY)}
    return engine.analyze_game(g, FakeEngine(), deep=True)


def setup(tmp_path):
    y = TODAY - datetime.timedelta(days=1)
    recs = [make("a1", SCHOLAR, False, y, "checkmated", "win"),
            make("a2", FREE, True, y, "win", "resigned", "rapid"),
            make("a3", QUEEN, True, y, "resigned", "win"),
            make("o1", QUEEN, True, y - datetime.timedelta(days=3), "resigned", "win", "rapid")]
    os.makedirs(tmp_path / "data" / "v2")
    with open(tmp_path / "data" / "v2" / "games.jsonl", "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    json.dump({"total": {"blitz": 2, "rapid": 2}, "exclues": {}, "echecs": []},
              open(tmp_path / "data" / "v2" / "manifest.json", "w"))
    render.render(TODAY, root=str(tmp_path))
    return {n: open(tmp_path / n, encoding="utf-8").read() for n in ("seance.md", "corriges.md", "rapport.md", "profil.md")}


def test_la_seance_ne_contient_aucune_solution(tmp_path):
    f = setup(tmp_path)
    s = f["seance.md"].split("## Leçon du jour")[0]
    for interdit in ("Meilleur coup", "Pourquoi", "Ton coup", "Ligne conseillée", "(corrigé)", "mat subi",
                     "pièce laissée en prise", "gain de matériel manqué"):
        assert interdit not in s, interdit
    assert "Question :" in s and "Leçon du jour" in f["seance.md"]
    assert f["seance.md"].index("## Positions de la séance") < f["seance.md"].index("## Leçon du jour")


def test_les_corriges_contiennent_la_solution(tmp_path):
    c = setup(tmp_path)["corriges.md"]
    assert "Meilleur coup" in c and "Pourquoi" in c and "Ce qui se passe après ton coup" in c


def test_aucun_echiquier_texte_et_liens_lichess_exacts(tmp_path):
    f = setup(tmp_path)
    for name, text in f.items():
        assert "```" not in text, name
        assert not re.search(r"^[1-8]  [.#a-zA-Z] ", text, re.M), name
    for text in (f["seance.md"], f["rapport.md"]):
        pairs = re.findall(r"- Échiquier : (\S+)\n- FEN : (.+)", text)
        for url, fen in pairs:
            assert chess.Board(fen).is_valid()
            assert url.split("analysis/")[1].split("?")[0].replace("_", " ") == fen
            assert url.endswith("?color=black") == (chess.Board(fen).turn == chess.BLACK)


def test_rapport_couvre_toutes_les_parties_de_la_veille(tmp_path):
    r = setup(tmp_path)["rapport.md"]
    assert r.count("## Partie ") == 3
    assert "Bishops Opening Berlin Defense" in r and "par mat" in r


def test_revision_d_une_ancienne_erreur(tmp_path):
    s = setup(tmp_path)["seance.md"]
    assert "révision d'une erreur d'il y a 3 jours" in s


def test_import_incomplet_est_signale(tmp_path):
    setup(tmp_path)
    m = {"total": {"blitz": 2, "rapid": 2}, "exclues": {}, "echecs": ["zzz"]}
    json.dump(m, open(tmp_path / "data" / "v2" / "manifest.json", "w"))
    render.render(TODAY, root=str(tmp_path))
    assert "ANALYSE INCOMPLÈTE" in open(tmp_path / "seance.md", encoding="utf-8").read()


def test_journee_sans_partie(tmp_path):
    os.makedirs(tmp_path / "data" / "v2")
    open(tmp_path / "data" / "v2" / "games.jsonl", "w").close()
    out = render.render(TODAY, root=str(tmp_path))
    assert "Aucune position exploitable" in "\n".join(out["seance.md"])


def test_accords_et_formulations(tmp_path):
    f = setup(tmp_path)
    tout = f["corriges.md"] + f["rapport.md"]
    assert "prise de le" not in tout and "prise de la" not in tout.replace("prise de la dame", "")
    assert "cavalier noir en d5 : il n'était pas défendu" in tout
