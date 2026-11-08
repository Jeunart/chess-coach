# Partie 3 du 2026-11-07

## Partie 3 : rapide - nulle par matériel insuffisant
- Lien : https://www.chess.com/game/live/186702150532

- Rapide (10 min), tu jouais les noirs contre besotooskinny (442) : nulle par matériel insuffisant.
- Ouverture : Queens Pawn Opening Chigorin.
- Au coup 10, la position était à peu près égale.
- Au coup 20, la position était nettement meilleure pour l'adversaire.
- Au coup 30, la position était perdante pour toi.
- 5 erreurs décisives de ta part (perte d'au moins 2 pions).
- L'adversaire t'a offert 5 occasions d'avantage ; tu en as saisi 2.
- Théorie d'ouverture : Au coup 4 des blancs, l'adversaire a joué Nc3 au lieu de Bd3 (coup du livret). Avant, la partie suivait la ligne « Principale » (Caro-Kann : variante d'échange (3.exd5)). Ligne complète et position finale : theorie.md.

### Moment clé 3.1 (corrigé)
- Partie : https://www.chess.com/game/live/186702150532 - coup 16, tu jouais les noirs
- Ton coup : le fou noir va de f8 en d6 (Bd6)
- Meilleur coup : la dame noire va de b8 en b7 (Qb7)
- Perte mesurée : 2.8 pion(s) ; évaluation -0.4 avant, -3.2 après (profondeur 18)
- Pourquoi : Le coup adverse Nc6+ attaque en même temps la dame noire en b8 et le roi noir en d8 : c'est une fourchette.
- Thème (étiquette automatique, approximative) : fourchette subie
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le cavalier blanc va de e5 en c6 (échec) (Nc6+) - la dame noire en b8 est attaquée par une pièce de moindre valeur
  2. le roi noir va de d8 en d7 (Kd7) - le cavalier blanc en c6 est attaqué et n'est pas défendu
  3. le cavalier blanc va de c6 en b8 et prend la dame noire (échec) (Nxb8+) - prise de la dame noire
  4. la tour noire va de a8 en b8 et prend le cavalier blanc (Raxb8) - prise du cavalier blanc
- Ligne conseillée par le moteur, coup par coup :
  1. la dame noire va de b8 en b7 (Qb7)
  2. la dame blanche va de d1 en f3 (Qf3) - le cavalier noir en f4 est attaqué et n'est pas défendu
  3. le cavalier noir va de f4 en h5 (Nh5)
  4. le cavalier blanc va de c3 en d5 et prend le pion noir (Nxd5) - prise du pion noir
  5. le fou noir va de f8 en d6 (Bd6) - le cavalier blanc en d5 est attaqué par une pièce de moindre valeur
- Autre option solide : la dame noire va de b8 en d6 (Qd6) (évaluation -0.5)
- Autre option solide : la dame noire va de b8 en c7 (Qc7) (évaluation -0.5)
- Temps restant sur ton horloge : 6:27

### Moment clé 3.2 (corrigé)
- Partie : https://www.chess.com/game/live/186702150532 - coup 26, tu jouais les noirs
- Ton coup : la tour noire va de b8 en c8 (Rbc8)
- Meilleur coup : le fou noir va de e5 en d4 (échec) (Bd4+)
- Perte mesurée : 3.0 pion(s) ; évaluation +3.2 avant, +0.2 après (profondeur 18)
- Pourquoi : Pas de tactique immédiate : ton coup a surtout dégradé ta position ; le meilleur coup donnait échec.
- Thème (étiquette automatique, approximative) : erreur positionnelle
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la tour blanche va de a1 en d1 (Rad1)
  2. la tour noire va de c8 en c2 et prend le pion blanc (échec) (Rxc2+) - prise du pion blanc
  3. le fou blanc va de b3 en c2 et prend la tour noire (Bxc2) - prise de la tour noire
  4. le fou noir va de g6 en c2 et prend le fou blanc (Bxc2) - prise du fou blanc ; la tour blanche en d1 est attaquée par une pièce de moindre valeur
- Ligne conseillée par le moteur, coup par coup :
  1. le fou noir va de e5 en d4 (échec) (Bd4+)
  2. le roi blanc va de f2 en f3 (Kf3) - la tour noire en b8 est attaquée par une pièce de moindre valeur
  3. la tour noire va de b8 en e8 (Rbe8)
  4. le fou blanc va de b3 en d5 et prend le cavalier noir (Bxd5) - prise du cavalier noir
  5. le roi noir va de d6 en d5 et prend le fou blanc (Kxd5) - prise du fou blanc
- Autre option solide : la tour noire va de b8 en b5 (Rb5) (évaluation +3.2)
- Autre option solide : le fou noir va de e5 en b2 et prend le pion blanc (Bxb2) (évaluation +3.1)
- Temps restant sur ton horloge : 4:08

### Moment clé 3.3 (corrigé)
- Partie : https://www.chess.com/game/live/186702150532 - coup 29, tu jouais les noirs
- Ton coup : le roi noir va de d6 en e6 (Ke6)
- Meilleur coup : le roi noir va de d6 en e7 (Ke7)
- Perte mesurée : 10.1 pion(s) ; évaluation +0.1 avant, mat en 3 pour l'adversaire après (profondeur 18)
- Pourquoi : Après ton coup, l'adversaire avait un mat en 3 coups.
- Thème (étiquette automatique, approximative) : mat subi
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la tour blanche va de f1 en e1 (échec) (Re1+)
  2. le fou noir va de c2 en e4 (Be4) - la tour blanche en d5 est attaquée par une pièce de moindre valeur
  3. la tour blanche va de e1 en e4 et prend le fou noir (échec) (Rxe4+) - prise du fou noir
  4. le fou noir va de b2 en e5 (Be5)
- Ligne conseillée par le moteur, coup par coup :
  1. le roi noir va de d6 en e7 (Ke7)
  2. le cavalier blanc va de a6 en b4 et prend le pion noir (Nxb4) - prise du pion noir
  3. le fou noir va de c2 en b3 et prend le fou blanc (Bxb3) - prise du fou blanc ; la tour blanche en d5 est attaquée par une pièce de moindre valeur
  4. le pion blanc va de a2 en b3 et prend le fou noir (axb3) - prise du fou noir
  5. le pion noir va de h7 en h6 (h6)
- Autre option solide : le roi noir va de d6 en c6 (Kc6) (évaluation -4.5)
- Autre option solide : le roi noir va de d6 en e6 (Ke6) (évaluation mat en 3 pour l'adversaire)
- Temps restant sur ton horloge : 3:37

