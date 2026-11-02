import collections

import digest
import picks


def profile(games):
    n = max(len(games), 1)
    errs = [e for g in games for e in g["errs"]]
    big = [e for g in games for e in picks.decisive(g)]
    tags = collections.Counter(e["tag"] for e in big)
    phases = collections.Counter(e["phase"] for e in big)
    short = sum(1 for e in big if e["clk"] is not None and e["clk"] < 60)
    wins = sum(g["result"] == "win" for g in games)
    L = ["# Profil durable (parties rapides analysées par Stockfish)", "",
         f"- Parties : {len(games)} ; victoires {wins} ({100 * wins // n} %)",
         f"- Bourdes décisives (perte >= 2 pions, position pas déjà perdue) : {len(big)}, soit {len(big) / n:.1f} par partie",
         f"- Erreurs moyennes (1 à 2 pions) : {sum(1 for e in errs if e['loss'] < 200)}",
         f"- Bourdes décisives avec moins d'une minute à l'horloge : {short}", "", "## Types de bourdes"]
    L += [f"- {picks.TAGS[t]} : {c} ({100 * c // max(len(big), 1)} %)" for t, c in tags.most_common()]
    L += ["", "## Phase où je bourde"] + [f"- {p} : {c}" for p, c in phases.most_common()]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    open("data/profil.md", "w", encoding="utf-8").write(profile(digest.load()))
