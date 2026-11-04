"""Livret d'ouvertures de l'élève : lignes classiques, idées, pièges. Sert à theorie.md et au repérage
de la sortie de théorie dans chaque partie.

Les lignes sont des repères pédagogiques écrits à la main (connaissance générale des ouvertures) ; leur
légalité est vérifiée par les tests, leur évaluation exacte ne l'est pas : le coach les présente comme
« ligne classique », jamais comme une vérité du moteur.
"""
import chess

from coach import facts

# (identifiant, couleur de l'élève, titre, idée en une phrase, [(nom de la ligne, coups SAN, remarque)])
BOOK = [
    ("scotch", "blancs", "Partie écossaise (Scotch)",
     "J'ouvre le centre tout de suite : je prends avec le cavalier en d4 et je développe vite mes pièces.",
     [("Principale", "1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Nf6 5.Nxc6 bxc6 6.e5 Qe7 7.Qe2 Nd5 8.c4",
       "Les noirs ont des pions doublés ; je chasse le cavalier d5."),
      ("4...Fc5", "1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Be3 Qf6 6.c3 Nge7 7.Bc4",
       "Je protège mon cavalier d4 avec c3 et je développe le fou en c4."),
      ("4...Dh4", "1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Qh4 5.Nc3 Bb4 6.Nxc6",
       "La dame sort trop tôt : je développe en attaquant elle.")]),
    ("italienne", "blancs", "Partie italienne et Deux cavaliers",
     "Le fou en c4 vise f7, le point faible des noirs ; je roque vite et je prépare c3 et d3 ou d4.",
     [("Giuoco Pianissimo", "1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d3 d6 6.O-O O-O 7.Re1 a6",
       "Plan calme : développer, roquer, puis d3 et Cd2-f1."),
      ("Deux cavaliers (Cg5)", "1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5+ c6 7.dxc6 bxc6 8.Be2 h6 9.Nf3 e4 10.Ne5",
       "Je gagne un pion mais il faut défendre juste ; ne pas jouer Cxf7 trop vite."),
      ("Piège : Fried Liver (à connaître)", "1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nxd5 6.Nxf7 Kxf7 7.Qf3+ Ke6 8.Nc3",
       "Sacrifice de cavalier en f7 : le roi noir est poursuivi au centre."),
      ("Piège : Legal", "1.e4 e5 2.Nf3 d6 3.Bc4 Bg4 4.Nc3 g6 5.Nxe5 Bxd1 6.Bxf7+ Ke7 7.Nd5#",
       "Si les noirs prennent la dame, je mate avec le fou et le cavalier.")]),
    ("anti-scandinave", "blancs", "Contre la Scandinave (1.e4 d5)",
     "Je reprends le pion d5, j'évite de perdre du temps et je développe en chassant la dame.",
     [("2...Dxd5", "1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 Nf6 5.Nf3 c6 6.Bc4 Bf5 7.Bd2 e6",
       "La dame noire est chassée : je développe avec avance et je roque."),
      ("2...Cf6", "1.e4 d5 2.exd5 Nf6 3.d4 Nxd5 4.Nf3 g6 5.Bc4 Nb6 6.Bb3 Bg7",
       "Le centre est à moi ; je garde le fou actif en b3.")]),
    ("anti-philidor", "blancs", "Contre la Philidor (1.e4 d6)",
     "Les noirs jouent passif ; je prends le centre, je développe et je roque.",
     [("Principale", "1.e4 d6 2.d4 Nf6 3.Nc3 e5 4.Nf3 Nbd7 5.Bc4 Be7 6.O-O O-O 7.a4",
       "Je gagne de l'espace sur l'aile dame avant de passer à l'attaque.")]),
    ("englund", "blancs", "Contre le Gambit Englund (1.d4 e5)",
     "Les noirs sacrifient un pion pour piéger ; je prends le pion et je ne tombe pas dans le piège de la dame.",
     [("Principale", "1.d4 e5 2.dxe5 Nc6 3.Nf3 Qe7 4.Bf4 Qb4+ 5.Bd2 Qxb2 6.Bc3 Bb4 7.Qd2",
       "Le piège classique : les noirs prennent b2 ; je réponds par Fc3 puis Dd2.")]),
    ("london", "blancs", "Système de Londres",
     "Je développe le fou en f4 avant e3, puis je construis la même position quoi que fasse l'adversaire.",
     [("Contre 1...d5", "1.d4 d5 2.Bf4 Nf6 3.e3 e6 4.Nf3 Bd6 5.Bg3 O-O 6.Nbd2 c5 7.c3 Nc6 8.Bd3",
       "Pion en c3, cavalier en d2, fou en d3, puis roque."),
      ("Contre 1...Cf6", "1.d4 Nf6 2.Bf4 e6 3.e3 Be7 4.Nf3 O-O 5.h3",
       "Le pion h3 donne une case de repli au fou f4.")]),
    ("caro-classique", "noirs", "Caro-Kann : variante classique (3.Cc3)",
     "Je prends en e4, je sors mon fou AVANT de jouer e6, puis je m'organise solidement.",
     [("Principale", "1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7 9.Bd3 Bxd3 10.Qxd3 e6 11.Bf4 Ngf6 12.O-O-O Be7",
       "Mon fou est dehors avant e6 : c'est la raison d'être du Caro-Kann.")]),
    ("caro-avance", "noirs", "Caro-Kann : variante d'avance (3.e5)",
     "Je sors mon fou avant de fermer avec e6, puis j'attaque le centre blanc avec c5.",
     [("Principale", "1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 c5",
       "Le fou est dehors ; je casse le centre blanc avec c5.")]),
    ("caro-echange", "noirs", "Caro-Kann : variante d'échange (3.exd5)",
     "Structure symétrique ; je développe calmement et je surveille les clouages en g4 et f4.",
     [("Principale", "1.e4 c6 2.d4 d5 3.exd5 cxd5 4.Bd3 Nc6 5.c3 Nf6 6.Bf4 Bg4",
       "Le fou noir sort avant e6 ; je vérifie chaque case avant de jouer.")]),
    ("caro-panov", "noirs", "Caro-Kann : attaque Panov (4.c4)",
     "Les blancs veulent un pion isolé ou une position ouverte ; je développe et j'échange.",
     [("Principale", "1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.Nc3 e6 6.Nf3 Bb4 7.cxd5 Nxd5 8.Bd2 Nc6 9.Bd3 Nf6 10.O-O O-O",
       "Je développe vite et je roque ; je surveille le pion isolé en d5.")]),
    ("caro-deux-cavaliers", "noirs", "Caro-Kann : deux cavaliers (2.Cc3)",
     "Je prends le centre avec d5 et je sors mon fou en g4 pour le placer activement.",
     [("Principale", "1.e4 c6 2.Nc3 d5 3.Nf3 Bg4 4.h3 Bxf3 5.Qxf3 e6",
       "J'échange le fou contre un cavalier et je construis une structure solide.")]),
    ("francaise", "noirs", "Défense française",
     "Pions e6 et d5 ; je prépare une cassure en c5 et je sors mon fou-dame avec soin.",
     [("Classique (3.Cc3)", "1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7 7.f4 O-O 8.Nf3 c5",
       "Je casse le centre avec c5."),
      ("Avance (3.e5)", "1.e4 e6 2.d4 d5 3.e5 c5 4.c3 Nc6 5.Nf3 Qb6",
       "Je mets la pression sur d4 : c5, Cc6, Db6."),
      ("Échange (3.exd5)", "1.e4 e6 2.d4 d5 3.exd5 exd5 4.Nf3 Nf6 5.Bd3 Bd6 6.O-O O-O 7.Bg5 Bg4",
       "Structure symétrique : je développe et je clouerai le cavalier f3."),
      ("Tarrasch (3.Cd2)", "1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.Bd3 c5 6.c3 Nc6 7.Ne2 cxd4 8.cxd4 f6",
       "Je mets le centre blanc sous pression avec c5 puis f6.")]),
    ("scandinave", "noirs", "Défense scandinave (1...d5)",
     "Je prends le pion d5 avec la dame ; je dois la mettre à l'abri sans perdre de temps.",
     [("Principale", "1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 Nf6 5.Nf3 c6 6.Bc4 Bf5",
       "La dame est en a5 : je développe fou et cavalier.")]),
    ("vs-1d4", "noirs", "Contre 1.d4 : Londres et Gambit dame",
     "Je prends le centre avec d5 et je développe avec ordre, sans copier l'adversaire.",
     [("Contre Londres", "1.d4 d5 2.Bf4 Nf6 3.e3 c5 4.c3 Nc6 5.Nd2 e6 6.Ngf3 Bd6 7.Bg3 O-O",
       "Je casse le centre avec c5 et je garde mes pièces actives."),
      ("Gambit dame refusé", "1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7",
       "Position classique, solide ; je roque et je prépare c5 ou e5.")]),
    ("vs-reti", "noirs", "Contre 1.Cf3 / Réti",
     "Je prends le centre avec d5 et je développe symétriquement, sans me précipiter.",
     [("Principale", "1.Nf3 d5 2.g3 Nf6 3.Bg2 e6 4.O-O Be7",
       "Position calme ; je roque et je cherche une cassure en c5.")]),
]

PRINCIPLES = [
    "Prendre le centre avec un ou deux pions (e4/d4 pour les blancs ; d5, e5 ou c5 pour les noirs).",
    "Sortir une pièce mineure à chaque coup, sans bouger deux fois la même pièce sans raison.",
    "Roquer vite (idéalement avant le coup 10).",
    "Ne pas sortir la dame trop tôt.",
    "À chaque coup : « Que menace-t-il ? Ma pièce déplacée est-elle défendue ? »",
]


def _moves(txt):
    return [t.split(".")[-1] for t in txt.split() if t.split(".")[-1]]


def entries():
    """Chaque ligne avec ses coups SAN, le FEN final et le lien Lichess."""
    out = []
    for oid, side, title, idea, lines in BOOK:
        for name, txt, note in lines:
            sans = _moves(txt)
            b = chess.Board()
            for s in sans:
                b.push_san(s)
            out.append({"oid": oid, "side": side, "title": title, "idea": idea, "name": name,
                        "text": txt, "sans": sans, "fen": b.fen(), "link": facts.lichess(b.fen()), "note": note})
    return out


def build_md():
    L = ["# Livret d'ouvertures de Dimitri", "",
         "Lignes classiques et idées, écrites à la main : des repères pédagogiques, pas des vérités du moteur. "
         "Le coach les présente comme « ligne classique ». Notation des coups : N = cavalier, B = fou, R = tour, Q = dame, K = roi, O-O = petit roque, x = prise, + = échec. Les liens Lichess ouvrent la position à la fin de chaque ligne (moteur éteint).", "",
         "## Les 5 principes d'ouverture"]
    L += [f"- {p}" for p in PRINCIPLES] + [""]
    ents = entries()
    for side in ("blancs", "noirs"):
        L += [f"# Quand je joue les {side}", ""]
        done = []
        for e in ents:
            if e["side"] != side:
                continue
            if e["oid"] not in done:
                done.append(e["oid"])
                L += [f"## {e['title']}", f"Idée : {e['idea']}", ""]
            L += [f"- {e['name']} : {e['text']}", f"  - À retenir : {e['note']}", f"  - Position finale (Lichess) : {e['link']}"]
        L.append("")
    return L


def deviation(g, sans, ents=None):
    """Compare la partie au livret : ligne la plus proche, coup où l'on quitte la théorie, qui a dévié."""
    ents = ents or entries()
    best, best_n = None, 0
    for e in ents:
        if e["side"] != ("blancs" if g["white"] else "noirs"):
            continue
        n = 0
        for a, b in zip(sans, e["sans"]):
            if a != b:
                break
            n += 1
        if n > best_n:
            best, best_n = e, n
    if best is None or best_n < 4:
        return None
    if best_n >= min(len(sans), len(best["sans"])):
        return {"line": best, "plies": best_n, "left": None}
    nxt = best["sans"][best_n]
    who = "toi" if (best_n % 2 == 0) == g["white"] else "l'adversaire"
    return {"line": best, "plies": best_n, "left": {"ply": best_n + 1, "who": who, "played": sans[best_n], "book": nxt}}


def deviation_text(g, sans):
    d = deviation(g, sans)
    if d is None:
        return "Ouverture hors de mon livret : consulte l'ouverture dans theorie.md si elle y figure, sinon applique les 5 principes."
    ln = d["line"]
    if d["left"] is None:
        return f"Ta partie suit la ligne « {ln['name']} » ({ln['title']}) jusqu'au bout du livret : {d['plies']} demi-coups."
    lf = d["left"]
    mv = (lf["ply"] + 1) // 2
    couleur = "blancs" if lf["ply"] % 2 == 1 else "noirs"
    sujet = "tu as joué" if lf["who"] == "toi" else "l'adversaire a joué"
    return (f"Au coup {mv} des {couleur}, {sujet} {lf['played']} au lieu de {lf['book']} (coup du livret). "
            f"Avant, la partie suivait la ligne « {ln['name']} » ({ln['title']}). Ligne complète et position finale : theorie.md.")
