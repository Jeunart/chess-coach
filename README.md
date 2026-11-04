# chess-coach

Robot quotidien : importe toutes les parties chess.com de `jeunart` (bullet, blitz, rapide, par correspondance), les analyse avec Stockfish et prépare les fichiers lus par le professeur d'échecs (Projet ChatGPT).

## Fichiers produits (adresses stables sur `main`)
| Fichier | Contenu | Lu par le professeur |
|---|---|---|
| `seance.md` | bilan, récit des parties de la veille, positions à travailler (liens Lichess), **sans solutions** | au début de la séance |
| `corriges.md` | solutions, pourquoi, réfutation, lignes du moteur expliquées en mots | après la réponse de l'élève |
| `rapport.md` | analyse détaillée et expliquée de **chaque** partie de la veille | pour la revue des parties |
| `profil.md` | profil durable, tendances 7/30/90 jours | au besoin |
| `programme.md` | les leçons | pour le mini-cours |
| `archives/AAAA-MM-JJ/` | copie datée des quatre fichiers du jour | - |

## Principes
- Tout fait sur l'échiquier (pièce attaquée, défendue, prise, échec, mat) est calculé par `python-chess` ; les variantes viennent de Stockfish et sont conservées en UCI dans `data/v2/games.jsonl`. Le professeur ne calcule rien.
- Aucun échiquier en texte : chaque position a un lien Lichess construit depuis son FEN.
- Un import ou une analyse incomplète est signalé en tête des fichiers (`Contrôle des données`).

## Code
`coach/chesscom.py` (import) · `coach/engine.py` (analyse, passe 1 profondeur 12, passe approfondie 18 MultiPV 3 sur les erreurs décisives des 3 derniers jours) · `coach/facts.py` (faits et explication des erreurs) · `coach/report.py` · `coach/render.py` · `coach/profile.py` · `tests/`.

Lancer à la main : onglet Actions, workflow `analyse`, Run workflow (champ date facultatif).

`legacy` : `analyze_all.py`, `digest.py`, `engine.py`, `picks.py`, `resume.py`, `fetch_games.py`, `data/a3.jsonl`, `seances/` datent de la V1/V2 et ne sont plus utilisés par le workflow `analyse`.
