# Partie 4 du 2026-11-23

## Partie 4 : rapide - défaite par mat
- Lien : https://www.chess.com/game/live/187855940228

- Rapide (10 min), tu jouais les blancs contre 11aleksa (602) : défaite par mat.
- Ouverture : Scotch.
- Au coup 10, la position était à peu près égale.
- Au coup 20, la position était à peu près égale.
- 3 erreurs décisives de ta part (perte d'au moins 2 pions).
- L'adversaire t'a offert 2 occasions d'avantage ; tu en as saisi 0.
- Théorie d'ouverture : Au coup 3 des noirs, l'adversaire a joué Nxd4 au lieu de exd4 (coup du livret). Avant, la partie suivait la ligne « Principale » (Partie écossaise (Scotch)). Ligne complète et position finale : theorie.md.

### Moment clé 4.1 (corrigé)
- Partie : https://www.chess.com/game/live/187855940228 - coup 12, tu jouais les blancs
- Ton coup : la dame blanche va de e5 en e4 (Qe4)
- Meilleur coup : la dame blanche va de e5 en e7 et prend le fou noir (Qxe7)
- Perte mesurée : 5.1 pion(s) ; évaluation +5.2 avant, +0.1 après (profondeur 18)
- Pourquoi : Après ton coup, une pièce restée sans défense (le fou blanc en g5) n'était pas défendu : l'adversaire la prend avec Bxg5.
- Thème (étiquette automatique, approximative) : pièce laissée en prise
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le fou noir va de e7 en g5 et prend le fou blanc (Bxg5) - prise du fou blanc
  2. la dame blanche va de e4 en g4 et prend le fou noir (Qxg4) - prise du fou noir
  3. le cavalier noir va de d7 en e5 (Ne5) - la dame blanche en g4 est attaquée et n'est pas défendue
  4. la dame blanche va de g4 en e4 (Qe4) - le cavalier noir en e5 est attaqué et n'est pas défendu
- Ligne conseillée par le moteur, coup par coup :
  1. la dame blanche va de e5 en e7 et prend le fou noir (Qxe7) - prise du fou noir
  2. la dame noire va de d8 en e7 et prend la dame blanche (Qxe7) - prise de la dame blanche ; le fou blanc en g5 est attaqué et n'est pas défendu
  3. le fou blanc va de g5 en e7 et prend la dame noire (Bxe7) - prise de la dame noire ; la tour noire en f8 est attaquée par une pièce de moindre valeur
  4. le cavalier noir va de d7 en e5 (Ne5) - le fou blanc en c4 est attaqué et n'est pas défendu
  5. le fou blanc va de c4 en b3 (Bb3) - la tour noire en f8 est attaquée par une pièce de moindre valeur
- Autre option solide : le fou blanc va de g5 en e7 et prend le fou noir (Bxe7) (évaluation +0.2)
- Autre option solide : la dame blanche va de e5 en e4 (Qe4) (évaluation +0.1)
- Temps restant sur ton horloge : 7:39

### Moment clé 4.2 (corrigé)
- Partie : https://www.chess.com/game/live/187855940228 - coup 21, tu jouais les blancs
- Ton coup : la dame blanche va de g4 en b4 (Qb4)
- Meilleur coup : le pion blanc va de h2 en h3 (h3)
- Perte mesurée : 3.2 pion(s) ; évaluation -0.5 avant, -3.8 après (profondeur 18)
- Pourquoi : Pas de gain immédiat pour l'adversaire, mais après b5 (dans la suite du moteur) le cavalier blanc en a4 est attaqué par une pièce de moindre valeur : ton coup te fait perdre du temps et de l'initiative.
- Thème (étiquette automatique, approximative) : erreur positionnelle
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le pion noir va de b7 en b5 (b5) - le cavalier blanc en a4 est attaqué par une pièce de moindre valeur
  2. le cavalier blanc va de a4 en c5 (Nc5)
  3. le fou noir va de f6 en e7 (Be7)
  4. la tour blanche va de d7 en e7 et prend le fou noir (Rxe7) - prise du fou noir ; la dame noire en e5 est attaquée et n'est pas défendue
- Ligne conseillée par le moteur, coup par coup :
  1. le pion blanc va de h2 en h3 (h3)
  2. le pion noir va de b7 en b5 (b5) - le cavalier blanc en a4 est attaqué par une pièce de moindre valeur
  3. le cavalier blanc va de a4 en c3 (Nc3)
  4. le pion noir va de h7 en h5 (h5) - la dame blanche en g4 est attaquée par une pièce de moindre valeur
  5. la dame blanche va de g4 en f3 (Qf3)
- Autre option solide : le pion blanc va de g2 en g3 (g3) (évaluation -0.8)
- Autre option solide : la tour blanche va de d1 en f1 (Rf1) (évaluation -1.0)
- Temps restant sur ton horloge : 5:08

### Moment clé 4.3 (corrigé)
- Partie : https://www.chess.com/game/live/187855940228 - coup 24, tu jouais les blancs
- Ton coup : la tour blanche va de d8 en d7 (Rd7)
- Meilleur coup : la tour blanche va de d8 en e8 et prend la tour noire (échec) (Rxe8+)
- Perte mesurée : 9.6 pion(s) ; évaluation -0.4 avant, mat en 2 pour l'adversaire après (profondeur 18)
- Pourquoi : Après ton coup, l'adversaire avait un mat en 2 coups.
- Thème (étiquette automatique, approximative) : mat subi
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la dame noire va de e5 en e1 (échec) (Qe1+) - la dame blanche en b4 est attaquée et n'est pas défendue
  2. la dame blanche va de b4 en e1 et prend la dame noire (Qxe1) - prise de la dame noire ; la tour noire en e8 est attaquée et n'est pas défendue
  3. la tour noire va de e8 en e1 et prend la dame blanche (échec et mat) (Rxe1#) - prise de la dame blanche
- Ligne conseillée par le moteur, coup par coup :
  1. la tour blanche va de d8 en e8 et prend la tour noire (échec) (Rxe8+) - prise de la tour noire ; la dame noire en e5 est attaquée par une pièce de moindre valeur
  2. la dame noire va de e5 en e8 et prend la tour blanche (Qxe8) - prise de la tour blanche
  3. le pion blanc va de g2 en g3 (g3)
  4. le pion noir va de h7 en h5 (h5)
  5. le cavalier blanc va de a4 en c3 (Nc3)
- Autre option solide : la tour blanche va de d8 en d1 (Rd1) (évaluation -3.1)
- Autre option solide : le pion blanc va de g2 en g3 (g3) (évaluation -5.7)
- Temps restant sur ton horloge : 4:35

