# Séance coach - 2026-11-02

## Bilan (30 dernières parties rapides)
- Classement : 431 -> 447 ; victoires : 17/30
- Bourdes décisives par partie : 4.0 (30 parties précédentes : 2.3)

## Parties du 2026-11-01 (revue)
- https://www.chess.com/game/live/186335487836 : noirs, gagnée, 3 bourdes décisives
- https://www.chess.com/game/live/186335903718 : blancs, nulle, 8 bourdes décisives
- https://www.chess.com/game/live/186363792120 : blancs, perdue, 4 bourdes décisives
- https://www.chess.com/game/live/186364396708 : noirs, perdue, 2 bourdes décisives
Moments critiques (position jouable où j'ai perdu l'avantage) :
Pour chaque position : montre l'échiquier tel quel, puis pose la question ; les coups sont décrits en mots avant la notation.
Légende des échiquiers : MAJUSCULES = pièces blanches, minuscules = pièces noires ; K/k roi, Q/q dame, R/r tour, B/b fou, N/n cavalier, P/p pion ; . = case vide. Notation des coups : K Roi, Q Dame, R Tour, B Fou, N Cavalier, aucune lettre = pion ; x = prise ; + = échec ; # = mat ; O-O = petit roque ; O-O-O = grand roque.

### Moment 1 : https://www.chess.com/game/live/186335487836 coup 12, trait aux noirs (noirs en bas de l'échiquier)
```
1  R . B K Q B N R
2  . . . . . P . .
3  . . . . . . P .
4  P . P . N . n P
5  p P . P p . . .
6  . b . p . . q .
7  . p p . . . p p
8  r n b k . . . r
   h g f e d c b a
```
Blancs : Roi e1, Dame d1, Tours a1 h1, Fous c1 f1, Cavaliers b1 d4, Pions a4 b3 c2 e5 f4 g5 h4
Noirs : Roi e8, Dame b6, Tours a8 h8, Fous f8 g6, Cavaliers b4 g8, Pions a7 b7 d5 e6 f7 g7 h5
FEN : r3kbnr/pp3pp1/1q2p1b1/3pP1Pp/Pn1N1P1P/1P6/2P5/RNBQKB1R b KQkq - 0 12
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : la dame noire va de b6 en c5 (Qc5)
- Ligne du moteur (meilleur coup en premier) : 1) la dame noire va de b6 en d4 et prend le cavalier blanc (Qxd4) 2) le fou blanc va de f1 en b5 (échec) (Bb5+) 3) le roi noir va de e8 en d8 (Kd8) 4) la dame blanche va de d1 en d4 et prend la dame noire (Qxd4) 5) le cavalier noir va de b4 en c2 et prend le pion blanc (échec) (Nxc2+)
- Perte : 5.4 pions ; type d'erreur : gain de pièce manqué

### Moment 2 : https://www.chess.com/game/live/186335487836 coup 14, trait aux noirs (noirs en bas de l'échiquier)
```
1  R . . K Q B N R
2  . . . . . P . .
3  . . . . . . P .
4  P . . . N . n P
5  p P P P p q B .
6  . b . p . . . .
7  . p p k . . p p
8  r n b . . . . r
   h g f e d c b a
```
Blancs : Roi e1, Dame d1, Tours a1 h1, Fous b5 c1, Cavaliers b1 d4, Pions a4 b3 c2 e5 f5 g5 h4
Noirs : Roi e7, Dame c5, Tours a8 h8, Fous f8 g6, Cavaliers b4 g8, Pions a7 b7 d5 e6 f7 g7 h5
FEN : r4bnr/pp2kpp1/4p1b1/1BqpPPPp/Pn1N3P/1P6/2P5/RNBQK2R b KQ - 0 14
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le cavalier noir va de b4 en c2 et prend le pion blanc (échec) (Nxc2+)
- Ligne du moteur (meilleur coup en premier) : 1) la dame noire va de c5 en d4 et prend le cavalier blanc (Qxd4) 2) la dame blanche va de d1 en d4 et prend la dame noire (Qxd4) 3) le cavalier noir va de b4 en c2 et prend le pion blanc (échec) (Nxc2+) 4) le roi blanc va de e1 en d2 (Kd2) 5) le cavalier noir va de c2 en d4 et prend la dame blanche (Nxd4)
- Perte : 6.5 pions ; type d'erreur : pièce laissée en prise

### Moment 3 : https://www.chess.com/game/live/186335903718 coup 23, trait aux blancs (blancs en bas de l'échiquier)
```
8  r . . . . . . .
7  . . . . n . p p
6  . . . . Q p k .
5  . . . . . . . .
4  B . . . P . . .
3  . . P . . P . .
2  P P . . . K P P
1  R N . . . . . q
   a b c d e f g h
```
Blancs : Roi f2, Dame e6, Tour a1, Fou a4, Cavalier b1, Pions a2 b2 c3 e4 f3 g2 h2
Noirs : Roi g6, Dame h1, Tour a8, Cavalier e7, Pions f6 g7 h7
FEN : r7/4n1pp/4Qpk1/8/B3P3/2P2P2/PP3KPP/RN5q w - - 3 23
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le fou blanc va de a4 en c6 (Bc6)
- Ligne du moteur (meilleur coup en premier) : 1) la dame blanche va de e6 en e7 et prend le cavalier noir (Qxe7) 2) la dame noire va de h1 en c1 (Qc1) 3) la dame blanche va de e7 en b4 (Qb4) 4) la tour noire va de a8 en d8 (Rd8) 5) la dame blanche va de b4 en c5 (Qc5)
- Perte : 2.9 pions ; type d'erreur : pièce laissée en prise

### Moment 4 : https://www.chess.com/game/live/186335903718 coup 69, trait aux blancs (blancs en bas de l'échiquier)
```
8  . . . . . . . .
7  . . . . . . . .
6  . . . . . . . .
5  . . . . . . . .
4  . . K . . . . .
3  . . Q . . . . .
2  . . . . . . . .
1  . k . . . . . .
   a b c d e f g h
```
Blancs : Roi c4, Dame c3
Noirs : Roi b1
FEN : 8/8/8/8/2K5/2Q5/8/1k6 w - - 25 69
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le roi blanc va de c4 en b3 (Kb3)
- Ligne du moteur (meilleur coup en premier) : 1) la dame blanche va de c3 en e1 (échec) (Qe1+) 2) le roi noir va de b1 en c2 (Kc2) 3) la dame blanche va de e1 en e2 (échec) (Qe2+) 4) le roi noir va de c2 en b1 (Kb1) 5) le roi blanc va de c4 en c3 (Kc3)
- Perte : 10.0 pions ; type d'erreur : mat manqué


## Puzzles tirés de mes anciennes bourdes (solution après ma réponse)
### Puzzle 1 : https://www.chess.com/game/live/174189643854 coup 15, trait aux noirs (noirs en bas de l'échiquier)
```
1  R N B K . B R .
2  P . . . . . P P
3  . . P n . . . .
4  Q . . P p . . N
5  P . . . . . . .
6  . . n p b . . p
7  . p p . . p p .
8  . k r . q . . r
   h g f e d c b a
```
Blancs : Roi e1, Dame h4, Tours b1 h1, Fous c1 f1, Cavaliers a4 g1, Pions a2 b2 e4 f3 h2 h5
Noirs : Roi g8, Dame d8, Tours a8 f8, Fou d6, Cavaliers e3 f6, Pions a6 b7 c7 d4 e6 f7 g7
FEN : r2q1rk1/1pp2pp1/p2bpn2/7P/N2pP2Q/4nP2/PP5P/1RB1KBNR b - - 2 15
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le cavalier noir va de e3 en g4 (Neg4)
- Ligne du moteur (meilleur coup en premier) : 1) le fou noir va de d6 en b4 (échec) (Bb4+) 2) le fou blanc va de c1 en d2 (Bd2) 3) la dame noire va de d8 en d6 (Qd6) 4) le fou blanc va de d2 en b4 et prend le fou noir (Bxb4) 5) la dame noire va de d6 en b4 et prend le fou blanc (échec) (Qxb4+)
- Perte : 4.3 pions

### Puzzle 2 : https://www.chess.com/game/live/184914489554 coup 15, trait aux blancs (blancs en bas de l'échiquier)
```
8  r . . . k . . r
7  p p p . . p p p
6  . . . . . . . .
5  . . q n . b B .
4  . b N . . . . .
3  . B . P . P . .
2  P P . . . . P P
1  R N . Q . R K .
   a b c d e f g h
```
Blancs : Roi g1, Dame d1, Tours a1 f1, Fous b3 g5, Cavaliers b1 c4, Pions a2 b2 d3 f3 g2 h2
Noirs : Roi e8, Dame c5, Tours a8 h8, Fous b4 f5, Cavalier d5, Pions a7 b7 c7 f7 g7 h7
FEN : r3k2r/ppp2ppp/8/2qn1bB1/1bN5/1B1P1P2/PP4PP/RN1Q1RK1 w kq - 4 15
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le cavalier blanc va de c4 en e3 (Ne3)
- Ligne du moteur (meilleur coup en premier) : 1) le pion blanc va de d3 en d4 (d4) 2) la dame noire va de c5 en c6 (Qc6) 3) le cavalier blanc va de c4 en e5 (Ne5) 4) la dame noire va de c6 en b6 (Qb6) 5) le fou blanc va de b3 en d5 et prend le cavalier noir (Bxd5)
- Perte : 4.0 pions

### Puzzle 3 : https://www.chess.com/game/live/184906018678 coup 7, trait aux blancs (blancs en bas de l'échiquier)
```
8  r . b q k . . r
7  p p p p . . p p
6  . . n . . . . .
5  . . . . . . . .
4  . b . . n B . .
3  . . . . P N . .
2  P P P . . P P P
1  R N . Q K B . R
   a b c d e f g h
```
Blancs : Roi e1, Dame d1, Tours a1 h1, Fous f1 f4, Cavaliers b1 f3, Pions a2 b2 c2 e3 f2 g2 h2
Noirs : Roi e8, Dame d8, Tours a8 h8, Fous b4 c8, Cavaliers c6 e4, Pions a7 b7 c7 d7 g7 h7
FEN : r1bqk2r/pppp2pp/2n5/8/1b2nB2/4PN2/PPP2PPP/RN1QKB1R w KQkq - 1 7
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le cavalier blanc va de b1 en c3 (Nc3)
- Ligne du moteur (meilleur coup en premier) : 1) le pion blanc va de c2 en c3 (c3) 2) le fou noir va de b4 en c5 (Bc5) 3) le cavalier blanc va de b1 en d2 (Nbd2) 4) le cavalier noir va de e4 en f6 (Nf6) 5) le pion blanc va de b2 en b4 (b4)
- Perte : 4.1 pions


## Focus et mini-cours : pièce laissée en prise
Avant chaque coup : la pièce que je déplace est-elle protégée ? Une autre pièce reste-t-elle sans défense ?
