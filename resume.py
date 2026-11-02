import collections
import json

TAGS = {"mat_subi": "mat subi (j'ai laissé un mat)", "mat_rate": "mat manqué",
        "piece_en_prise": "pièce laissée en prise", "gain_rate": "gain de pièce manqué",
        "autre": "autre erreur positionnelle ou tactique"}


def load(path="data/analysis.jsonl"):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def profile(games):
    n = len(games)
    errs = [e for g in games for e in g["errs"]]
    big = [e for e in errs if e["loss"] >= 200]
    tags = collections.Counter(e["tag"] for e in big)
    phases = collections.Counter(e["phase"] for e in big)
    short = sum(1 for e in big if e["clk"] is not None and e["clk"] < 60)
    res = collections.Counter(g["result"] for g in games)
    wins = res["win"]
    L = ["# Profil durable (parties rapides analysées par Stockfish)", "",
         f"- Parties : {n} ; victoires {wins} ({100 * wins // max(n, 1)} %)",
         f"- Bourdes (perte >= 2 pions) : {len(big)}, soit {len(big) / max(n, 1):.1f} par partie",
         f"- Erreurs moyennes (1 à 2 pions) : {len(errs) - len(big)}",
         f"- Bourdes avec moins d'une minute à l'horloge : {short}", "", "## Types de bourdes"]
    for t, c in tags.most_common():
        L.append(f"- {TAGS[t]} : {c} ({100 * c // max(len(big), 1)} %)")
    L += ["", "## Phase de la partie où je bourde"]
    for p, c in phases.most_common():
        L.append(f"- {p} : {c}")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    open("data/profil.md", "w", encoding="utf-8").write(profile(load()))
