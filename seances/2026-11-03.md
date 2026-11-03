# Séance coach - 2026-11-03

## Bilan (30 dernières parties rapides)
- Classement : 453 -> 446 ; victoires : 15/30
- Bourdes décisives par partie : 4.2 (30 parties précédentes : 2.5)

## Parties du 2026-11-02 (revue)
- https://www.chess.com/game/live/186397478940 : blancs, perdue, 2 bourdes décisives
- https://www.chess.com/game/live/186407415698 : noirs, gagnée, 1 bourdes décisives
- https://www.chess.com/game/live/186410635090 : blancs, gagnée, 1 bourdes décisives
- https://www.chess.com/game/live/186412330258 : blancs, perdue, 2 bourdes décisives
- https://www.chess.com/game/live/186423864720 : noirs, perdue, 7 bourdes décisives
- https://www.chess.com/game/live/186424612566 : blancs, gagnée, 6 bourdes décisives
- https://www.chess.com/game/live/186425109780 : blancs, gagnée, 4 bourdes décisives
- https://www.chess.com/game/live/186425761594 : blancs, perdue, 1 bourdes décisives
Moments critiques (position jouable où j'ai perdu l'avantage) :
Pour chaque position : montre l'échiquier tel quel, puis pose la question ; les coups sont décrits en mots avant la notation.
Légende des échiquiers : MAJUSCULES = pièces blanches, minuscules = pièces noires ; K/k roi, Q/q dame, R/r tour, B/b fou, N/n cavalier, P/p pion ; . = case claire vide, # = case foncée vide. Notation des coups : K Roi, Q Dame, R Tour, B Fou, N Cavalier, aucune lettre = pion ; x = prise ; + = échec ; # = mat ; O-O = petit roque ; O-O-O = grand roque.

### Moment 1 : https://www.chess.com/game/live/186397478940 coup 11, trait aux blancs (blancs en bas de l'échiquier)
```
8  r # . # k # . r
7  p b p p # p p p
6  . p . # . q . #
5  # B b n P . # .
4  . # . # . # . #
3  # . # . # . # .
2  P P P Q . P P P
1  R N B . # R K .
   a b c d e f g h
```
Blancs : Roi g1, Dame d2, Tours a1 f1, Fous b5 c1, Cavalier b1, Pions a2 b2 c2 e5 f2 g2 h2
Noirs : Roi e8, Dame f6, Tours a8 h8, Fous b7 c5, Cavalier d5, Pions a7 b6 c7 d7 f7 g7 h7
FEN : r3k2r/pbpp1ppp/1p3q2/1BbnP3/8/8/PPPQ1PPP/RNB2RK1 w kq - 5 11
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : la dame blanche va de d2 en e2 (Qe2)
- Ligne du moteur (meilleur coup en premier) : 1) le pion blanc va de e5 en f6 et prend la dame noire (exf6) 2) le roi fait le grand roque (O-O-O) 3) la dame blanche va de d2 en d3 (Qd3) 4) le cavalier noir va de d5 en f6 et prend le pion blanc (Nxf6) 5) la dame blanche va de d3 en g3 (Qg3)
- Perte : 6.4 pions ; type d'erreur : gain de pièce manqué

### Moment 2 : https://www.chess.com/game/live/186397478940 coup 12, trait aux blancs (blancs en bas de l'échiquier)
```
8  r # . # k # . r
7  p b p p # p p p
6  . p . # . # q #
5  # B b n P . # .
4  . # . # . # . #
3  # . # . # . # .
2  P P P # Q P P P
1  R N B . # R K .
   a b c d e f g h
```
Blancs : Roi g1, Dame e2, Tours a1 f1, Fous b5 c1, Cavalier b1, Pions a2 b2 c2 e5 f2 g2 h2
Noirs : Roi e8, Dame g6, Tours a8 h8, Fous b7 c5, Cavalier d5, Pions a7 b6 c7 d7 f7 g7 h7
FEN : r3k2r/pbpp1ppp/1p4q1/1BbnP3/8/8/PPP1QPPP/RNB2RK1 w kq - 7 12
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le fou blanc va de c1 en f4 (Bf4)
- Ligne du moteur (meilleur coup en premier) : 1) la dame blanche va de e2 en f3 (Qf3) 2) le roi fait le grand roque (O-O-O) 3) le fou blanc va de b5 en d3 (Bd3) 4) la dame noire va de g6 en e6 (Qe6) 5) le fou blanc va de d3 en e4 (Be4)
- Perte : 8.4 pions ; type d'erreur : mat subi

### Moment 3 : https://www.chess.com/game/live/186407415698 coup 17, trait aux noirs (noirs en bas de l'échiquier)
```
1  R # B K . B . R
2  P P # . # . P P
3  . # P Q . P . N
4  # b # . # . # .
5  . # . # p # p #
6  # . n . b . # p
7  p p p # q # . #
8  # k r . # . # r
   h g f e d c b a
```
Blancs : Roi e1, Dame e3, Tours a1 h1, Fous c1 f1, Cavalier a3, Pions a2 b2 c3 f3 g2 h2
Noirs : Roi g8, Dame d7, Tours a8 f8, Fous d6 g4, Cavalier f6, Pions a6 b5 d5 f7 g7 h7
FEN : r4rk1/3q1ppp/p2b1n2/1p1p4/6b1/N1P1QP2/PP4PP/R1B1KB1R b KQ - 0 17
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le fou noir va de g4 en h5 (Bh5)
- Ligne du moteur (meilleur coup en premier) : 1) la tour noire va de a8 en e8 (Rae8) 2) le pion blanc va de f3 en g4 et prend le fou noir (fxg4) 3) le fou noir va de d6 en c5 (Bc5) 4) le cavalier blanc va de a3 en c2 (Nc2) 5) le fou noir va de c5 en e3 et prend la dame blanche (Bxe3)
- Perte : 3.2 pions ; type d'erreur : autre erreur

### Moment 4 : https://www.chess.com/game/live/186410635090 coup 8, trait aux blancs (blancs en bas de l'échiquier)
```
8  r n b # k # . r
7  p p p p # p p p
6  . # . # . # q #
5  # . b . p . # .
4  . # B # P # . B
3  # . # P # N # P
2  P P P # . n P #
1  R N # Q K . # R
   a b c d e f g h
```
Blancs : Roi e1, Dame d1, Tours a1 h1, Fous c4 h4, Cavaliers b1 f3, Pions a2 b2 c2 d3 e4 g2 h3
Noirs : Roi e8, Dame g6, Tours a8 h8, Fous c5 c8, Cavaliers b8 f2, Pions a7 b7 c7 d7 e5 f7 g7 h7
FEN : rnb1k2r/pppp1ppp/6q1/2b1p3/2B1P2B/3P1N1P/PPP2nP1/RN1QK2R w KQkq - 0 8
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le cavalier blanc va de f3 en e5 et prend le pion noir (Nxe5)
- Ligne du moteur (meilleur coup en premier) : 1) le fou blanc va de h4 en f2 et prend le cavalier noir (Bxf2) 2) la dame noire va de g6 en g2 et prend le pion blanc (Qxg2) 3) la tour blanche va de h1 en f1 (Rf1) 4) le pion noir va de d7 en d5 (d5) 5) le pion blanc va de e4 en d5 et prend le pion noir (exd5)
- Perte : 7.4 pions ; type d'erreur : pièce laissée en prise


## Puzzles tirés de mes anciennes bourdes (solution après ma réponse)
### Puzzle 1 : https://www.chess.com/game/live/173019407538 coup 12, trait aux blancs (blancs en bas de l'échiquier)
```
8  N # b # . k n r
7  p . # p # . p p
6  . p n b . p . #
5  # . # . # . # .
4  . # B # q # . #
3  # . # p # N # .
2  P P P B . P P P
1  R . # Q # R K .
   a b c d e f g h
```
Blancs : Roi g1, Dame d1, Tours a1 f1, Fous c4 d2, Cavaliers a8 f3, Pions a2 b2 c2 f2 g2 h2
Noirs : Roi f8, Dame e4, Tour h8, Fous c8 d6, Cavaliers c6 g8, Pions a7 b6 d3 d7 f6 g7 h7
FEN : N1b2knr/p2p2pp/1pnb1p2/8/2B1q3/3p1N2/PPPB1PPP/R2Q1RK1 w - - 0 12
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : la tour blanche va de f1 en e1 (Re1)
- Ligne du moteur (meilleur coup en premier) : 1) le fou blanc va de c4 en d3 et prend le pion noir (Bxd3) 2) la dame noire va de e4 en g4 (Qg4) 3) la tour blanche va de f1 en e1 (Re1) 4) le cavalier noir va de g8 en e7 (Nge7) 5) le pion blanc va de h2 en h3 (h3)
- Perte : 5.4 pions

### Puzzle 2 : https://www.chess.com/game/live/173446410912 coup 6, trait aux blancs (blancs en bas de l'échiquier)
```
8  r n b # k # n r
7  p p p p # p p p
6  . # . # . # . #
5  # B # . p . # .
4  . b . # . # . #
3  # . P q # N # .
2  P P . P . P P P
1  R N B Q # K # R
   a b c d e f g h
```
Blancs : Roi f1, Dame d1, Tours a1 h1, Fous b5 c1, Cavaliers b1 f3, Pions a2 b2 c3 d2 f2 g2 h2
Noirs : Roi e8, Dame d3, Tours a8 h8, Fous b4 c8, Cavaliers b8 g8, Pions a7 b7 c7 d7 e5 f7 g7 h7
FEN : rnb1k1nr/pppp1ppp/8/1B2p3/1b6/2Pq1N2/PP1P1PPP/RNBQ1K1R w kq - 2 6
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le roi blanc va de f1 en e1 (Ke1)
- Ligne du moteur (meilleur coup en premier) : 1) le fou blanc va de b5 en d3 et prend la dame noire (Bxd3) 2) le fou noir va de b4 en d6 (Bd6) 3) le pion blanc va de a2 en a4 (a4) 4) le cavalier noir va de g8 en e7 (Ne7) 5) le pion blanc va de b2 en b4 (b4)
- Perte : 9.2 pions

### Puzzle 3 : https://www.chess.com/game/live/184053717368 coup 20, trait aux noirs (noirs en bas de l'échiquier)
```
1  . K R # . # . #
2  P P P . # . # P
3  . # . P Q R . #
4  # . # . P . P .
5  . # . # p # N #
6  p . p p # . # n
7  . p . # q r p #
8  # k r . # . # .
   h g f e d c b a
```
Blancs : Roi g1, Dame d3, Tours c3 f1, Cavalier b5, Pions a2 b4 d4 e3 f2 g2 h2
Noirs : Roi g8, Dame d7, Tours c7 f8, Cavalier a6, Pions b7 d5 e6 f6 g7 h6
FEN : 5rk1/1prq2p1/n3pp1p/1N1p4/1P1P4/2RQP3/P4PPP/5RK1 b - - 2 20
À RÉVÉLER SEULEMENT APRÈS MA RÉPONSE :
- Mon coup : le pion noir va de e6 en e5 (e5)
- Ligne du moteur (meilleur coup en premier) : 1) la tour noire va de c7 en c3 et prend la tour blanche (Rxc3) 2) le cavalier blanc va de b5 en c3 et prend la tour noire (Nxc3) 3) le cavalier noir va de a6 en b4 et prend le pion blanc (Nxb4) 4) la dame blanche va de d3 en b1 (Qb1) 5) le cavalier noir va de b4 en c6 (Nc6)
- Perte : 3.8 pions


## Focus et mini-cours : pièce laissée en prise
Avant chaque coup : la pièce que je déplace est-elle protégée ? Une autre pièce reste-t-elle sans défense ?
