# Corrigés de la séance du 2026-11-10

À lire SEULEMENT après la réponse de l'élève, position par position.

### Position 1 (corrigé)
- Partie : https://www.chess.com/game/live/186829363654 - coup 11, tu jouais les noirs
- Ton coup : le cavalier noir va de b8 en c6 (Nc6)
- Meilleur coup : le fou noir va de g4 en f3 et prend le cavalier blanc (Bxf3)
- Perte mesurée : 2.1 pion(s) ; évaluation -0.9 avant, -3.0 après (profondeur 18)
- Pourquoi : Pas de gain immédiat pour l'adversaire, mais après Rfd1 (dans la suite du moteur) la dame noire en d8 est attaquée par une pièce de moindre valeur : ton coup te fait perdre du temps et de l'initiative.
- Thème (étiquette automatique, approximative) : erreur positionnelle
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le pion blanc va de d4 en c5 et prend le pion noir (dxc5) - prise du pion noir
  2. le fou noir va de g4 en f3 et prend le cavalier blanc (Bxf3) - prise du cavalier blanc
  3. le fou blanc va de e2 en f3 et prend le fou noir (Bxf3) - prise du fou noir
  4. la dame noire va de d8 en c7 (Qc7)
- Ligne conseillée par le moteur, coup par coup :
  1. le fou noir va de g4 en f3 et prend le cavalier blanc (Bxf3) - prise du cavalier blanc
  2. la dame blanche va de e3 en f3 et prend le fou noir (Qxf3) - prise du fou noir
  3. le cavalier noir va de b8 en c6 (Nc6)
  4. le pion blanc va de d4 en c5 et prend le pion noir (dxc5) - prise du pion noir
  5. le cavalier noir va de c6 en d4 (Nd4) - la dame blanche en f3 est attaquée par une pièce de moindre valeur
- Autre option solide : le pion noir va de c5 en d4 et prend le pion blanc (cxd4) (évaluation -1.5)
- Autre option solide : le cavalier noir va de b8 en d7 (Nd7) (évaluation -2.4)
- Temps restant sur ton horloge : 8:40

### Position 2 (corrigé)
- Partie : https://www.chess.com/game/live/186831379896 - coup 14, tu jouais les blancs
- Ton coup : le cavalier blanc va de e5 en f7 et prend le pion noir (Nxf7)
- Meilleur coup : le fou blanc va de c4 en f7 et prend le pion noir (échec) (Bxf7+)
- Perte mesurée : 6.8 pion(s) ; évaluation +3.7 avant, -3.1 après (profondeur 18)
- Pourquoi : Après ton coup, une pièce restée sans défense (le fou blanc en c4) n'était pas défendu : l'adversaire la prend avec Qxc4.
- Thème (étiquette automatique, approximative) : pièce laissée en prise
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la dame noire va de c7 en c4 et prend le fou blanc (Qxc4) - prise du fou blanc ; le cavalier blanc en f7 est attaqué et n'est pas défendu
  2. le cavalier blanc va de f7 en h8 et prend la tour noire (Nxh8) - prise de la tour noire
  3. le fou noir va de f8 en g7 (Bg7) - le cavalier blanc en h8 est attaqué et n'est pas défendu
  4. le cavalier blanc va de h8 en g6 et prend le pion noir (Nxg6) - prise du pion noir
- Ligne conseillée par le moteur, coup par coup :
  1. le fou blanc va de c4 en f7 et prend le pion noir (échec) (Bxf7+) - prise du pion noir
  2. le roi noir va de e8 en d8 (Kd8)
  3. le fou blanc va de f7 en g6 et prend le pion noir (Bxg6) - prise du pion noir ; le fou noir en f5 est attaqué et n'est pas défendu
  4. le pion noir va de e7 en e6 (e6)
  5. la dame blanche va de d1 en f3 (Qf3)
- Autre option solide : la dame blanche va de d1 en f3 (Qf3) (évaluation +3.0)
- Autre option solide : le fou blanc va de c1 en f4 (Bf4) (évaluation +2.7)
- Temps restant sur ton horloge : 7:42

### Position 3 (corrigé)
- Partie : https://www.chess.com/game/live/186831379896 - coup 31, tu jouais les blancs
- Ton coup : la dame blanche va de e1 en g3 et prend le cavalier noir (Qxg3)
- Meilleur coup : la dame blanche va de e1 en b4 et prend la dame noire (Qxb4)
- Perte mesurée : 8.4 pion(s) ; évaluation +3.4 avant, -5.0 après (profondeur 18)
- Pourquoi : Tu pouvais gagner la dame noire en b4 : elle n'était pas défendue.
- Thème (étiquette automatique, approximative) : gain de matériel manqué
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la dame noire va de b4 en c5 (Qc5) - la tour blanche en e3 est attaquée et n'est pas défendue
  2. la dame blanche va de g3 en f2 (Qf2)
  3. la tour noire va de g8 en e8 (Rge8)
  4. la tour blanche va de e3 en e8 et prend la tour noire (Rxe8) - prise de la tour noire ; la tour noire en d8 est attaquée et n'est pas défendue
- Ligne conseillée par le moteur, coup par coup :
  1. la dame blanche va de e1 en b4 et prend la dame noire (Qxb4) - prise de la dame noire
  2. le cavalier noir va de d7 en c5 (Nc5) - la tour blanche en d1 est attaquée et n'est pas défendue
  3. la tour blanche va de d1 en e1 (Rde1)
  4. le cavalier noir va de c5 en e6 (Ne6)
  5. la dame blanche va de b4 en b6 et prend le pion noir (Qxb6) - prise du pion noir
- Autre option solide : la tour blanche va de d1 en d7 et prend le cavalier noir (échec) (Rxd7+) (évaluation +0.8)
- Autre option solide : la dame blanche va de e1 en f2 (Qf2) (évaluation -5.3)
- Temps restant sur ton horloge : 4:32

### Position 4 (corrigé)
- Partie : https://www.chess.com/game/live/186837015534 - coup 22, tu jouais les blancs
- Ton coup : la tour blanche va de e6 en e7 (échec) (Re7+)
- Meilleur coup : la tour blanche va de e6 en d6 (Rd6)
- Perte mesurée : 9.1 pion(s) ; évaluation +4.0 avant, -5.1 après (profondeur 18)
- Pourquoi : Après ton coup, l'adversaire gagne la tour blanche en e7 avec Bxe7 (échange défavorable pour toi).
- Thème (étiquette automatique, approximative) : pièce laissée en prise
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le fou noir va de f6 en e7 et prend la tour blanche (Bxe7) - prise de la tour blanche
  2. le pion blanc va de g2 en g4 (g4)
  3. le pion noir va de h7 en h6 (h6)
  4. le pion blanc va de g4 en g5 (g5)
- Ligne conseillée par le moteur, coup par coup :
  1. la tour blanche va de e6 en d6 (Rd6)
  2. le fou noir va de f6 en b2 et prend le pion blanc (Bxb2) - prise du pion blanc
  3. la tour blanche va de d6 en d5 et prend le pion noir (Rxd5) - prise du pion noir
  4. le fou noir va de b2 en d4 (Bd4)
  5. la tour blanche va de d5 en d7 (échec) (Rd7+)
- Autre option solide : le roi blanc va de g1 en f1 (Kf1) (évaluation +3.4)
- Autre option solide : le pion blanc va de b2 en b3 (b3) (évaluation +3.2)
- Temps restant sur ton horloge : 8:13

### Position 5 (corrigé)
- Partie : https://www.chess.com/game/live/186840232008 - coup 6, tu jouais les blancs
- Ton coup : le pion blanc va de e4 en e5 (e5)
- Meilleur coup : le cavalier blanc va de d4 en e6 (Ne6)
- Perte mesurée : 3.0 pion(s) ; évaluation +4.7 avant, +1.7 après (profondeur 18)
- Pourquoi : Pas de gain immédiat pour l'adversaire, mais après c6 (dans la suite du moteur) le fou blanc en b5 est attaqué par une pièce de moindre valeur : ton coup te fait perdre du temps et de l'initiative.
- Thème (étiquette automatique, approximative) : erreur positionnelle
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le pion noir va de c7 en c6 (c6) - le fou blanc en b5 est attaqué par une pièce de moindre valeur
  2. le fou blanc va de b5 en e2 (Be2)
  3. le fou noir va de f8 en g7 (Bg7)
  4. le roi fait le petit roque (O-O)
- Ligne conseillée par le moteur, coup par coup :
  1. le cavalier blanc va de d4 en e6 (Ne6) - la dame noire en d8 est attaquée par une pièce de moindre valeur
  2. la dame noire va de d8 en e7 (Qe7) - le cavalier blanc en e6 est attaqué et n'est pas défendu
  3. le cavalier blanc va de e6 en c7 et prend le pion noir (échec) (Nxc7+) - prise du pion noir ; la tour noire en a8 est attaquée et n'est pas défendue
  4. le roi noir va de e8 en d8 (Kd8) - le cavalier blanc en c7 est attaqué et n'est pas défendu
  5. le fou blanc va de c1 en g5 (Bg5) - la tour noire en a8 est attaquée et n'est pas défendue ; la dame noire en e7 est attaquée par une pièce de moindre valeur
- Autre option solide : le pion blanc va de e4 en f5 et prend le pion noir (exf5) (évaluation +3.1)
- Autre option solide : le roi fait le petit roque (O-O) (évaluation +3.0)
- Temps restant sur ton horloge : 4:42

### Position 6 (corrigé)
- Partie : https://www.chess.com/game/live/186842567942 - coup 11, tu jouais les noirs
- Ton coup : le pion noir va de e6 en e5 (e5)
- Meilleur coup : le fou noir va de d6 en f4 et prend le fou blanc (Bxf4)
- Perte mesurée : 5.9 pion(s) ; évaluation +1.5 avant, -4.3 après (profondeur 18)
- Pourquoi : Après ton coup, l'adversaire gagne le fou noir en d6 avec Nxd6+ (échange défavorable pour toi).
- Thème (étiquette automatique, approximative) : pièce laissée en prise
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le cavalier blanc va de b5 en d6 et prend le fou noir (échec) (Nxd6+) - prise du fou noir
  2. le roi noir va de e8 en f8 (Kf8) - le cavalier blanc en d6 est attaqué et n'est pas défendu ; le fou blanc en f4 est attaqué par une pièce de moindre valeur ; le cavalier blanc en h3 est attaqué et n'est pas défendu
  3. le cavalier blanc va de d6 en f7 et prend le pion noir (Nxf7) - prise du pion noir ; la tour noire en h8 est attaquée et n'est pas défendue ; la dame noire en d8 est attaquée et n'est pas défendue
  4. la dame noire va de d8 en a5 (échec) (Qa5+) - le cavalier blanc en f7 est attaqué et n'est pas défendu ; le fou blanc en f4 est attaqué par une pièce de moindre valeur ; le cavalier blanc en h3 est attaqué et n'est pas défendu
- Ligne conseillée par le moteur, coup par coup :
  1. le fou noir va de d6 en f4 et prend le fou blanc (Bxf4) - prise du fou blanc ; le cavalier blanc en h3 est attaqué et n'est pas défendu
  2. le cavalier blanc va de h3 en f4 et prend le fou noir (Nxf4) - prise du fou noir
  3. le pion noir va de a7 en a6 (a6) - le cavalier blanc en b5 est attaqué par une pièce de moindre valeur
  4. le cavalier blanc va de b5 en a3 (Na3)
  5. le pion noir va de c5 en d4 et prend le pion blanc (cxd4) - prise du pion blanc
- Autre option solide : la dame noire va de d8 en a5 (échec) (Qa5+) (évaluation -0.5)
- Autre option solide : le fou noir va de d6 en e7 (Be7) (évaluation -1.9)
- Temps restant sur ton horloge : 8:01

### Position 7 (corrigé)
- Partie : https://www.chess.com/game/live/186842567942 - coup 22, tu jouais les noirs
- Ton coup : le cavalier noir va de c6 en e5 (Ne5)
- Meilleur coup : la tour noire va de f8 en e8 (Rfe8)
- Perte mesurée : 9.2 pion(s) ; évaluation -0.8 avant, mat en 5 pour l'adversaire après (profondeur 18)
- Pourquoi : Après ton coup, l'adversaire avait un mat en 5 coups.
- Thème (étiquette automatique, approximative) : mat subi
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le cavalier blanc va de d5 en e7 (échec) (Ne7+)
  2. le roi noir va de g8 en h8 (Kh8)
  3. la dame blanche va de e2 en g2 (Qg2)
  4. le cavalier noir va de e5 en g4 et prend le pion blanc (Nxg4) - prise du pion blanc
- Ligne conseillée par le moteur, coup par coup :
  1. la tour noire va de f8 en e8 (Rfe8)
  2. le pion blanc va de f5 en f6 (f6)
  3. le pion noir va de b5 en c4 et prend le pion blanc (bxc4) - prise du pion blanc
  4. la tour blanche va de a1 en d1 (Rad1)
  5. le cavalier noir va de b4 en d5 et prend le cavalier blanc (Nxd5) - prise du cavalier blanc
- Autre option solide : le cavalier noir va de b4 en d5 et prend le cavalier blanc (Nxd5) (évaluation -1.2)
- Autre option solide : le pion noir va de b5 en c4 et prend le pion blanc (bxc4) (évaluation -1.3)
- Temps restant sur ton horloge : 3:19

### Position 8 (corrigé)
- Partie : https://www.chess.com/game/live/186843589822 - coup 13, tu jouais les blancs
- Ton coup : le fou blanc va de d4 en c3 (Bc3)
- Meilleur coup : le cavalier blanc va de g1 en f3 (Nf3)
- Perte mesurée : 5.7 pion(s) ; évaluation +5.2 avant, -0.5 après (profondeur 18)
- Pourquoi : Après ton coup, l'adversaire gagne le fou blanc en c3 avec bxc3 (échange défavorable pour toi).
- Thème (étiquette automatique, approximative) : pièce laissée en prise
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le pion noir va de b4 en c3 et prend le fou blanc (bxc3) - prise du fou blanc
  2. le roi fait le grand roque (O-O-O)
  3. la dame noire va de f5 en f4 (échec) (Qf4+)
  4. la dame blanche va de e2 en e3 (Qe3) - la dame noire en f4 est attaquée et n'est pas défendue
- Ligne conseillée par le moteur, coup par coup :
  1. le cavalier blanc va de g1 en f3 (Nf3)
  2. le roi fait le grand roque (O-O-O)
  3. le roi fait le petit roque (O-O) - le cavalier noir en e7 est attaqué et n'est pas défendu
  4. la tour noire va de h8 en e8 (Rhe8)
  5. le fou blanc va de d4 en e3 (Be3)
- Autre option solide : le fou blanc va de d4 en e3 (Be3) (évaluation +4.6)
- Autre option solide : le roi fait le grand roque (O-O-O) (évaluation +4.6)
- Temps restant sur ton horloge : 2:30

### Position 9 (corrigé)
- Partie : https://www.chess.com/game/live/186843589822 - coup 17, tu jouais les blancs
- Ton coup : le cavalier blanc va de d4 en b5 (Nb5)
- Meilleur coup : le roi fait le petit roque (O-O)
- Perte mesurée : 5.8 pion(s) ; évaluation +0.1 avant, -5.7 après (profondeur 18)
- Pourquoi : Pas de gain immédiat pour l'adversaire, mais après Nf5 (dans la suite du moteur) la dame blanche en e2 est attaquée par une pièce de moindre valeur : ton coup te fait perdre du temps et de l'initiative.
- Thème (étiquette automatique, approximative) : erreur positionnelle
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le cavalier noir va de e7 en f5 (Nf5) - la dame blanche en e2 est attaquée par une pièce de moindre valeur
  2. le roi fait le petit roque (O-O)
  3. la tour noire va de e8 en e2 et prend la dame blanche (Rxe2) - prise de la dame blanche ; le cavalier blanc en b5 est attaqué et n'est pas défendu
  4. le pion blanc va de c3 en c4 (c4) - la dame noire en d5 est attaquée et n'est pas défendue
- Ligne conseillée par le moteur, coup par coup :
  1. le roi fait le petit roque (O-O)
  2. le cavalier noir va de e7 en g6 (Ng6) - la dame blanche en e2 est attaquée par une pièce de moindre valeur
  3. la dame blanche va de e2 en b5 (Qb5) - la dame noire en d5 est attaquée et n'est pas défendue
  4. la dame noire va de d5 en e4 (Qe4)
  5. la dame blanche va de b5 en f5 (Qf5)
- Autre option solide : le roi blanc va de e1 en f1 (Kf1) (évaluation -1.0)
- Autre option solide : le roi fait le grand roque (O-O-O) (évaluation -1.1)
- Temps restant sur ton horloge : 1:47

### Position 10 (corrigé)
- Partie : https://www.chess.com/game/live/186855844572 - coup 19, tu jouais les blancs
- Ton coup : le fou blanc va de f4 en g5 (Bg5)
- Meilleur coup : la dame blanche va de a6 en a5 (échec) (Qa5+)
- Perte mesurée : 4.3 pion(s) ; évaluation -0.1 avant, -4.4 après (profondeur 18)
- Pourquoi : Pas de gain immédiat pour l'adversaire, mais après Ra8 (dans la suite du moteur) la dame blanche en a6 est attaquée et n'est pas défendue : ton coup te fait perdre du temps et de l'initiative.
- Thème (étiquette automatique, approximative) : erreur positionnelle
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la tour noire va de d8 en a8 (Ra8) - la dame blanche en a6 est attaquée et n'est pas défendue
  2. la dame blanche va de a6 en a8 et prend la tour noire (Qxa8) - prise de la tour noire ; la tour noire en h8 est attaquée et n'est pas défendue
  3. la tour noire va de h8 en a8 et prend la dame blanche (Rxa8) - prise de la dame blanche
  4. la tour blanche va de d1 en d3 (Rd3)
- Ligne conseillée par le moteur, coup par coup :
  1. la dame blanche va de a6 en a5 (échec) (Qa5+)
  2. le fou noir va de c5 en b6 (Bb6) - la dame blanche en a5 est attaquée et n'est pas défendue
  3. la dame blanche va de a5 en d2 (Qd2)
  4. le pion noir va de c6 en c5 (c5)
  5. le pion blanc va de c2 en c3 (c3)
- Autre option solide : la tour blanche va de d1 en d3 (Rd3) (évaluation -4.2)
- Autre option solide : le pion blanc va de h2 en h4 (h4) (évaluation -4.3)
- Temps restant sur ton horloge : 2:30

### Position 11 (corrigé)
- Partie : https://www.chess.com/game/live/186855844572 - coup 31, tu jouais les blancs
- Ton coup : le pion blanc va de b2 en b3 (b3)
- Meilleur coup : le fou blanc va de c2 en a4 et prend la tour noire (Bxa4)
- Perte mesurée : 8.3 pion(s) ; évaluation +3.9 avant, -4.4 après (profondeur 18)
- Pourquoi : Tu pouvais gagner la tour noire en a4 : elle n'était pas défendue.
- Thème (étiquette automatique, approximative) : gain de matériel manqué
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la tour noire va de a4 en a1 (échec) (Ra1+)
  2. le roi blanc va de c1 en b2 (Kb2) - la tour noire en a1 est attaquée et n'est pas défendue
  3. la tour noire va de a1 en g1 (Rg1)
  4. le pion blanc va de b3 en c4 et prend le pion noir (bxc4) - prise du pion noir
- Ligne conseillée par le moteur, coup par coup :
  1. le fou blanc va de c2 en a4 et prend la tour noire (Bxa4) - prise de la tour noire
  2. le pion noir va de c6 en c5 (c5) - la tour blanche en d4 est attaquée et n'est pas défendue
  3. la tour blanche va de d4 en d1 (Rd1)
  4. le pion noir va de f5 en f4 (f4)
  5. le fou blanc va de a4 en c2 (Bc2)
- Autre option solide : la tour blanche va de d4 en d1 (Rd1) (évaluation -3.7)
- Autre option solide : la tour blanche va de d4 en d7 (échec) (Rd7+) (évaluation -4.0)
- Temps restant sur ton horloge : 0:59 (moins d'une minute)

### Position 12 (corrigé)
- Partie : https://www.chess.com/game/live/186862350694 - coup 4, tu jouais les noirs
- Ton coup : le fou noir va de c8 en f5 (Bf5)
- Meilleur coup : le cavalier noir va de g8 en f6 (Nf6)
- Perte mesurée : 5.7 pion(s) ; évaluation +0.5 avant, -5.2 après (profondeur 18)
- Pourquoi : Après ton coup, la pièce que tu viens de déplacer (le fou noir en f5) n'était pas défendu : l'adversaire la prend avec Nxf5.
- Thème (étiquette automatique, approximative) : pièce laissée en prise
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le cavalier blanc va de d4 en f5 et prend le fou noir (Nxf5) - prise du fou noir
  2. le cavalier noir va de b8 en c6 (Nc6)
  3. le fou blanc va de f1 en b5 (Bb5)
  4. le pion noir va de e7 en e5 (e5)
- Ligne conseillée par le moteur, coup par coup :
  1. le cavalier noir va de g8 en f6 (Nf6)
  2. le fou blanc va de f1 en b5 (échec) (Bb5+)
  3. le cavalier noir va de b8 en d7 (Nbd7)
  4. le roi fait le petit roque (O-O)
  5. le pion noir va de a7 en a6 (a6) - le fou blanc en b5 est attaqué par une pièce de moindre valeur
- Autre option solide : le pion noir va de a7 en a6 (a6) (évaluation +0.4)
- Autre option solide : le pion noir va de e7 en e5 (e5) (évaluation +0.3)
- Temps restant sur ton horloge : 9:49

### Position 13 (corrigé)
- Partie : https://www.chess.com/game/live/186862350694 - coup 16, tu jouais les noirs
- Ton coup : la dame noire va de d7 en b5 et prend le fou blanc (Qxb5)
- Meilleur coup : le cavalier noir va de d4 en b5 et prend le fou blanc (Nxb5)
- Perte mesurée : 8.9 pion(s) ; évaluation +5.0 avant, -3.8 après (profondeur 18)
- Pourquoi : Après ton coup, l'adversaire gagne la dame noire en b5 avec Nxb5 (échange défavorable pour toi).
- Thème (étiquette automatique, approximative) : pièce laissée en prise
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le cavalier blanc va de a7 en b5 et prend la dame noire (Nxb5) - prise de la dame noire ; le cavalier noir en d4 est attaqué et n'est pas défendu
  2. le cavalier noir va de d4 en b5 et prend le cavalier blanc (Nxb5) - prise du cavalier blanc
  3. la dame blanche va de d2 en b4 (Qb4) - le cavalier noir en b5 est attaqué et n'est pas défendu
  4. le cavalier noir va de b5 en c7 (Nc7)
- Ligne conseillée par le moteur, coup par coup :
  1. le cavalier noir va de d4 en b5 et prend le fou blanc (Nxb5) - prise du fou blanc ; le cavalier blanc en a7 est attaqué et n'est pas défendu
  2. le cavalier blanc va de a7 en b5 et prend le cavalier noir (Nxb5) - prise du cavalier noir
  3. la dame noire va de d7 en b5 et prend le cavalier blanc (Qxb5) - prise du cavalier blanc
  4. la tour blanche va de f1 en e1 (Re1)
  5. le pion noir va de h7 en h6 (h6)
- Autre option solide : le cavalier noir va de d4 en c6 (Nc6) (évaluation -0.1)
- Autre option solide : la dame noire va de d7 en d6 (Qd6) (évaluation -3.5)
- Temps restant sur ton horloge : 8:14

### Position 14 (corrigé)
- Partie : https://www.chess.com/game/live/186644715678 - coup 16, tu jouais les noirs
- Ton coup : la dame noire va de b2 en a2 et prend le pion blanc (Qxa2)
- Meilleur coup : la dame noire va de b2 en c2 et prend le pion blanc (échec et mat) (Qxc2#)
- Perte mesurée : 14.9 pion(s) ; évaluation mat en 1 pour toi avant, -4.9 après (profondeur 18)
- Pourquoi : Tu avais un mat en 1 coup et ton coup l'a laissé passer.
- Thème (étiquette automatique, approximative) : mat manqué
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la tour blanche va de a1 en a2 et prend la dame noire (Rxa2) - prise de la dame noire
  2. la tour noire va de a8 en b8 (Rb8) - le cavalier blanc en b1 est attaqué et n'est pas défendu
  3. la tour blanche va de a2 en a1 (Ra1)
  4. le pion noir va de c5 en d4 et prend le pion blanc (cxd4) - prise du pion blanc ; le fou blanc en c3 est attaqué par une pièce de moindre valeur
- Ligne conseillée par le moteur, coup par coup :
  1. la dame noire va de b2 en c2 et prend le pion blanc (échec et mat) (Qxc2#) - prise du pion blanc
- Autre option solide : la dame noire va de b2 en b6 (Qb6) (évaluation +2.6)
- Autre option solide : la dame noire va de b2 en b5 (Qb5) (évaluation +2.2)
- Temps restant sur ton horloge : 5:58

### Position 15 (corrigé)
- Partie : https://www.chess.com/game/live/186397478940 - coup 12, tu jouais les blancs
- Ton coup : le fou blanc va de c1 en f4 (Bf4)
- Meilleur coup : la dame blanche va de e2 en f3 (Qf3)
- Perte mesurée : 8.0 pion(s) ; évaluation -1.2 avant, -9.2 après (profondeur 18)
- Pourquoi : Après ton coup, la pièce que tu viens de déplacer (le fou blanc en f4) n'était pas défendu : l'adversaire la prend avec Nxf4.
- Thème (étiquette automatique, approximative) : pièce laissée en prise
- Ce qui se passe après ton coup (ligne du moteur) :
  1. le cavalier noir va de d5 en f4 et prend le fou blanc (Nxf4) - prise du fou blanc ; la dame blanche en e2 est attaquée par une pièce de moindre valeur
  2. le fou blanc va de b5 en d7 et prend le pion noir (échec) (Bxd7+) - prise du pion noir
  3. le roi noir va de e8 en d7 et prend le fou blanc (Kxd7) - prise du fou blanc ; la dame blanche en e2 est attaquée et n'est pas défendue
  4. la dame blanche va de e2 en d3 (échec) (Qd3+)
- Ligne conseillée par le moteur, coup par coup :
  1. la dame blanche va de e2 en f3 (Qf3)
  2. le roi fait le grand roque (O-O-O)
  3. le fou blanc va de b5 en d3 (Bd3) - la dame noire en g6 est attaquée par une pièce de moindre valeur
  4. le pion noir va de f7 en f5 (f5)
  5. le pion blanc va de e5 en f6 et prend un pion en passant (exf6) - la dame noire en g6 est attaquée par une pièce de moindre valeur
- Autre option solide : la dame blanche va de e2 en d3 (Qd3) (évaluation -1.6)
- Autre option solide : le pion blanc va de g2 en g3 (g3) (évaluation -2.6)
- Temps restant sur ton horloge : 7:07

### Position 16 (corrigé)
- Partie : https://www.chess.com/game/live/185961051016 - coup 12, tu jouais les noirs
- Ton coup : la dame noire va de d5 en d4 (Qd4)
- Meilleur coup : le fou noir va de h5 en d1 et prend la dame blanche (Bxd1)
- Perte mesurée : 9.0 pion(s) ; évaluation +6.3 avant, -2.7 après (profondeur 12)
- Pourquoi : Tu pouvais gagner la dame blanche en d1 : tu la prenais avec une pièce de moindre valeur.
- Thème (étiquette automatique, approximative) : gain de matériel manqué
- Ce qui se passe après ton coup (ligne du moteur) :
  1. la dame blanche va de d1 en h5 et prend le fou noir (Qxh5) - prise du fou noir
  2. le roi fait le petit roque (O-O)
  3. le cavalier blanc va de h4 en f3 (Nf3) - la dame noire en d4 est attaquée par une pièce de moindre valeur
  4. la dame noire va de d4 en b2 et prend le pion blanc (Qxb2) - prise du pion blanc ; la tour blanche en a1 est attaquée et n'est pas défendue
- Ligne conseillée par le moteur, coup par coup :
  1. le fou noir va de h5 en d1 et prend la dame blanche (Bxd1) - prise de la dame blanche
  2. le roi blanc va de e1 en d1 et prend le fou noir (Kxd1) - prise du fou noir
  3. la dame noire va de d5 en d8 (Qd8) - le cavalier blanc en h4 est attaqué et n'est pas défendu
  4. la tour blanche va de a1 en c1 (Rc1) - le fou noir en c5 est attaqué et n'est pas défendu
  5. le fou noir va de c5 en f2 et prend le pion blanc (Bxf2) - prise du pion blanc ; le cavalier blanc en h4 est attaqué et n'est pas défendu
- Temps restant sur ton horloge : 4:14

