"""Génère le site de Jardinier Andrei (maquette).
  python3 outils/build.py artifact   -> /home/claude/andrei/artifact/ (accueil seul, CSS et JS intégrés, pour l'artefact)
  python3 outils/build.py site       -> pages HTML à la racine du dépôt
"""
import os, sys
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BASE = "https://webaunet.github.io/andrei-pintilii/"
TEL, TELH = "06 05 50 79 47", "+33605507947"
MAIL = "andreipintilii96@gmail.com"
ADR = "5 chemin des Écoliers, 78570 Andrésy"
NAME = "Jardinier Andrei"
MODE = sys.argv[1] if len(sys.argv) > 1 else "site"

ALT = {
    "andrei-pelouse-piscine": "Pelouse tondue en bandes le long d'une terrasse claire et d'une bordure de galets, avec une piscine couverte et des massifs au fond",
    "andrei-pelouse-terrasse": "Pelouse entretenue au pied d'une terrasse couverte, avec une haie taillée en arrière-plan",
    "andrei-abri-jardin": "Abri de jardin en bois foncé dans un sous-bois",
    "andrei-souche": "Terre retournée et souche d'arbre arrachée dans un jardin, avec une pelle posée au sol",
    "andrei-cloture-bois": "Panneaux de clôture en bois clair posés entre deux poteaux au fond d'un jardin",
    "creation-massifs": "Jardinier plantant au bord d'une pelouse à bordure courbe, devant une maison contemporaine et un massif de graminées",
    "entretien-pelouse": "Jardinier tondant la pelouse d'un jardin devant une maison en pierre aux volets bleus",
    "elagage-arbre": "Élagueur encordé, casqué, travaillant à la tronçonneuse dans un grand chêne au-dessus d'un jardin",
    "amenagement-terrasse": "Pose d'une terrasse en bois devant une maison en pierre",
    "plantation": "Jardinier à genoux plantant un arbuste dans un massif fraîchement ameubli",
}



def img(name, lazy=True, style=""):
    w, h = Image.open(os.path.join(ROOT, "images", name + ".jpg")).size
    return '<img src="images/%s.jpg" width="%d" height="%d" alt="%s"%s%s>' % (
        name, w, h, ALT[name], ' loading="lazy"' if lazy else "", ' style="%s"' % style if style else "")


def fig(name, cap, style=""):
    return "<figure>%s<figcaption class=\"cap\">%s</figcaption></figure>" % (img(name, style=style), cap)


PAGES = [("index.html", "Accueil"), ("services.html", "Services"), ("realisations.html", "Réalisations"), ("contact.html", "Contact")]


def nav(active):
    out = ""
    for h, t in PAGES:
        if MODE == "artifact" and h != "index.html":
            out += '<li><a href="#" data-soon="%s">%s</a></li>' % (t, t)
        else:
            out += '<li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if h == active else "", t)
    return out


def header(active):
    return f'''<a class="skip" href="#contenu">Aller au contenu</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="{BASE if MODE == "site" else "#accueil"}" aria-label="{NAME}, accueil">
      <img src="images/logo-palmier.png" width="62" height="39" alt="">
      <span><b>JARDINIER ANDREI</b><small>Paysagiste · Andrésy</small></span>
    </a>
    <nav id="menu" aria-label="Navigation principale"><ul>{nav(active)}</ul></nav>
    <a class="call" href="tel:{TELH}" aria-label="Appeler le {TEL}">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
      <span>{TEL}</span>
    </a>
    <button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu"><span></span></button>
  </div>
</header>'''


def footer():
    items = ""
    for h, t in PAGES[1:]:
        if MODE == "artifact":
            items += '<li><a href="#" data-soon="%s">%s</a></li>' % (t, t)
        else:
            items += '<li><a href="%s">%s</a></li>' % (h, t)
    ml = '<li class="m"><a href="#" data-soon="Mentions légales">Mentions légales</a></li>' if MODE == "artifact" else '<li class="m"><a href="mentions-legales.html">Mentions légales</a></li>'
    return f'''<footer>
  <div class="wrap">
    <div class="row">
      <div><b>JARDINIER ANDREI</b> <address>{ADR}</address></div>
      <ul aria-label="Liens du pied de page"><li class="t"><a href="tel:{TELH}">{TEL}</a></li>{items}{ml}</ul>
    </div>
    <div class="legal">© Andrei Pintilii · Maquette de site</div>
  </div>
</footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>'''


def home():
    return f'''
<main id="contenu">
  <section class="hero" id="accueil" aria-labelledby="t-hero">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Jardinier paysagiste · Andrésy (78)</span>
        <h1 id="t-hero">L'élégance <em>verte</em> à votre portée.</h1>
        <p class="lead">Andrei crée vos massifs et votre pelouse, entretient votre jardin, taille et élague vos arbres, et prend en charge les petits travaux d'aménagement extérieur.</p>
        <div class="actions">
          <a class="btn btn-sun" href="tel:{TELH}">Appeler Andrei</a>
          <a class="btn btn-line" href="#services">Les services</a>
        </div>
        <ul class="facts"><li>Entreprise individuelle créée en 2023</li><li>Un seul interlocuteur</li></ul>
      </div>
      <div class="arch">
        <div class="frame">{img("andrei-pelouse-piscine", lazy=False, style="object-position:50% 55%")}</div>
        <div class="badge" aria-hidden="true"><span><b>2023</b>création</span></div>
      </div>
    </div>
  </section>

  <section class="band bg-chalk" id="services" aria-labelledby="t-serv">
    <div class="wrap">
      <div class="head">
        <span class="eyebrow">Les services</span>
        <h2 id="t-serv">Créer, entretenir, élaguer, aménager</h2>
        <p>Du premier massif jusqu'à l'arbre à abattre, tout se règle avec la même personne.</p>
      </div>
      <div class="cards">
        <article class="card"><div class="ph">{img("creation-massifs")}</div><div class="in"><span class="pill p1">Créer</span><h3>Massifs et pelouse</h3><p>Un jardin imaginé selon vos envies, planté et engazonné.</p><ul><li>Création de massifs</li><li>Semis de pelouse ou gazon en rouleaux</li><li>Plantation de fleurs, arbres, arbustes et haies</li></ul></div></article>
        <article class="card"><div class="ph">{img("entretien-pelouse")}</div><div class="in"><span class="pill p2">Entretenir</span><h3>Entretien du jardin</h3><p>Le suivi régulier qui garde pelouse et massifs en forme.</p><ul><li>Tonte, désherbage, arrosage</li><li>Taille de haies, rosiers et arbustes</li><li>Ramassage des feuilles, débroussaillage</li></ul></div></article>
        <article class="card"><div class="ph">{img("elagage-arbre")}</div><div class="in"><span class="pill p3">Les arbres</span><h3>Élagage et abattage</h3><p>Des arbres qui gênent ou qui vieillissent, pris en charge.</p><ul><li>Abattage et élagage</li><li>Suppression des branches indésirables</li><li>Arrachage des souches</li></ul></div></article>
        <article class="card"><div class="ph">{img("amenagement-terrasse")}</div><div class="in"><span class="pill p4">Aménager</span><h3>Petits travaux extérieurs</h3><p>Un savoir-faire polyvalent pour finir votre extérieur.</p><ul><li>Accès, allées et terrasses</li><li>Maçonnerie paysagère, clôtures</li><li>Abri de jardin, peinture</li></ul></div></article>
      </div>
    </div>
  </section>

  <section class="band bg-sand" id="realisations" aria-labelledby="t-real">
    <div class="wrap">
      <div class="head">
        <span class="eyebrow">Sur le terrain</span>
        <h2 id="t-real">Des chantiers réalisés par Andrei</h2>
        <p>Quelques photos de chantiers publiées par Andrei sur sa fiche Google.</p>
      </div>
      <div class="mos">
        {fig("andrei-pelouse-terrasse", "Pelouse au pied d'une terrasse", "object-position:50% 70%")}
        {fig("andrei-abri-jardin", "Abri de jardin en bois")}
        {fig("andrei-cloture-bois", "Clôture en bois")}
        {fig("andrei-souche", "Chantier de dessouchage", "object-position:50% 40%")}
      </div>
      <div class="actions"><a class="btn btn-ink" {soon("realisations.html", "Réalisations")}>Voir toutes les réalisations</a></div>
    </div>
  </section>

  <section class="band bg-lawn" id="apropos" aria-labelledby="t-about">
    <div class="wrap">
      <div class="about">
        <div class="visual">{img("plantation", style="object-position:55% 50%")}</div>
        <div class="copy">
          <span class="eyebrow">Qui est Andrei</span>
          <h2 id="t-about">Un jardinier polyvalent, à Andrésy</h2>
          <p>Andrei Pintilii a créé son entreprise individuelle à Andrésy en 2023. Il s'occupe de la création et de l'entretien de votre jardin, des arbres, et des petits travaux d'aménagement extérieur.</p>
          <p>Pour toute question, vous le joignez directement par téléphone ou par e-mail.</p>
          <div class="ident"><span>Entreprise individuelle</span><span>SIREN 923 150 528</span><span>{ADR}</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="band cta bg-sun" id="contact" aria-labelledby="t-contact">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Contact</span>
        <h2 id="t-contact">Envie d'aménager votre jardin ?</h2>
        <p>Un besoin, une demande, un projet à réaliser ? Prenez rendez-vous avec Andrei dès aujourd'hui.</p>
        <span class="tel" id="tel-txt">{TEL}</span>
        <a class="mail" href="mailto:{MAIL}">{MAIL}</a>
        <address>{ADR}</address>
        <div class="actions">
          <a class="btn btn-ink" href="tel:{TELH}">Appeler</a>
          <a class="btn btn-ghost" href="mailto:{MAIL}">Écrire un e-mail</a>
          <button class="btn btn-ghost" type="button" id="copy">Copier le numéro</button>
        </div>
      </div>
      <img class="logo-big" src="images/logo-palmier.png" width="300" height="188" alt="" loading="lazy">
    </div>
  </section>
</main>'''


def _alt_more():
    return {
        "andrei-souche-2": "Terre retournée autour d'une souche arrachée, avec des plantes au pied",
        "nivellement-terrain": "Jardinier ratissant une terre fraîchement ameublie devant une maison en pierre et des massifs fleuris",
        "taille-haie": "Jardinier taillant une haie avec un taille-haie thermique dans un jardin devant une maison en brique",
        "desherbage-massif": "Jardinier accroupi désherbant un massif fleuri bordé de gravier, avec une brouette à côté",
        "feuilles-mortes": "Jardinier ratissant des feuilles mortes sur une bordure de gravier, avec des sacs de déchets verts",
        "dessouchage": "Souche d'arbre broyée par une machine de dessouchage jaune dans un jardin engazonné",
        "maconnerie-pierre": "Jardinier montant un muret et des marches en pierre dans un jardin en pente douce devant une maison",
        "allee-dallee": "Allée dallée en pierre claire bordée d'un muret de pierre et de massifs, devant une maison de campagne",
        "conception-plan": "Plan de jardin affiché sur une tablette, avec un jardin aménagé et un muret de pierre en arrière-plan",
    }


ALT.update(_alt_more())


def soon(href, label):
    if MODE == "artifact":
        return 'href="#" data-soon="%s"' % label
    return 'href="%s"' % href


def tf(name, cls="", style="", cap=None, lazy=True):
    return '<figure%s>%s%s</figure>' % (' class="%s"' % cls if cls else "", img(name, lazy=lazy, style=style),
                                         '<figcaption class="%s">%s</figcaption>' % ("cap2" if cap and cap.startswith("~") is False else "cap", cap) if cap else "")


def services():
    return f'''
<main id="contenu">
  <section class="phead bg-palm" aria-labelledby="t-h">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Services</span>
        <h1 id="t-h">Un jardin créé, entretenu et aménagé</h1>
        <p class="lead">Création de massifs et de pelouse, entretien, taille, élagage, abattage et petits travaux : tout se règle avec Andrei.</p>
        <div class="actions"><a class="btn btn-sun" href="tel:{TELH}">Appeler Andrei</a><a class="btn btn-line" href="#creer">Voir les prestations</a></div>
      </div>
      <div class="trio">
        {tf("creation-massifs", style="object-position:50% 50%", lazy=False)}
        {tf("entretien-pelouse", lazy=False)}
        {tf("elagage-arbre", style="object-position:50% 30%", lazy=False)}
      </div>
    </div>
  </section>

  <section class="band bg-chalk" id="creer" aria-labelledby="t-creer">
    <div class="wrap split">
      <div>
        <span class="eyebrow">Créer</span>
        <h2 id="t-creer">Massifs, pelouse et plantations</h2>
        <p>Un jardin imaginé selon vos envies, planté et engazonné : massifs, fleurs, arbres, arbustes et haies.</p>
        <ul class="ticks"><li>Création de massifs</li><li>Semis de pelouse</li><li>Gazon en rouleaux</li><li>Plantation de fleurs, arbres, arbustes et haies</li></ul>
        <div class="actions"><a class="btn btn-ink" href="tel:{TELH}">Demander conseil</a></div>
      </div>
      <div class="duo">{tf("plantation", style="object-position:55% 50%")}{tf("nivellement-terrain")}</div>
    </div>
  </section>

  <section class="band bg-sand" id="entretenir" aria-labelledby="t-ent">
    <div class="wrap split rev">
      <div>
        <span class="eyebrow">Entretenir</span>
        <h2 id="t-ent">Un jardin suivi toute l'année</h2>
        <p>Le suivi régulier qui garde pelouse, haies et massifs en forme.</p>
        <ul class="ticks"><li>Tonte de la pelouse</li><li>Désherbage et arrosage</li><li>Taille de haies, rosiers et arbustes</li><li>Ramassage des feuilles</li><li>Débroussaillage</li></ul>
        <div class="actions"><a class="btn btn-ink" href="tel:{TELH}">Demander un devis</a></div>
      </div>
      <div class="duo">{tf("taille-haie", style="object-position:50% 40%")}{tf("desherbage-massif")}</div>
    </div>
  </section>

  <section class="band bg-lawn" id="arbres" aria-labelledby="t-arb">
    <div class="wrap split">
      <div>
        <span class="eyebrow">Les arbres</span>
        <h2 id="t-arb">Élagage, abattage et souches</h2>
        <p>Un arbre qui gêne, des branches indésirables, une souche à enlever : Andrei s'en occupe.</p>
        <ul class="ticks"><li>Abattage et élagage</li><li>Suppression des branches indésirables</li><li>Arrachage des souches</li></ul>
        <div class="actions"><a class="btn btn-sun" href="tel:{TELH}">Appeler Andrei</a></div>
      </div>
      <div class="pair">
        <figure>{img("dessouchage", style="object-position:40% 50%")}</figure>
        <figure>{img("andrei-souche-2")}<figcaption class="cap2">Photo d'un chantier</figcaption></figure>
      </div>
    </div>
  </section>

  <section class="band bg-chalk" id="amenager" aria-labelledby="t-am">
    <div class="wrap split rev">
      <div>
        <span class="eyebrow">Aménager</span>
        <h2 id="t-am">Petits travaux d'aménagement extérieur</h2>
        <p>Un savoir-faire polyvalent pour finir votre extérieur, de l'accès à l'abri de jardin.</p>
        <ul class="ticks"><li>Accès, allées et terrasses</li><li>Maçonnerie paysagère</li><li>Clôtures</li><li>Abri de jardin</li><li>Peinture</li></ul>
        <div class="actions"><a class="btn btn-ink" href="tel:{TELH}">Demander un devis</a></div>
      </div>
      <div class="pair">
        <figure>{img("maconnerie-pierre", style="object-position:60% 50%")}</figure>
        <figure>{img("andrei-cloture-bois")}<figcaption class="cap2">Photo d'un chantier</figcaption></figure>
      </div>
    </div>
  </section>

  <section class="band band-ink cta2" id="contact" aria-labelledby="t-c">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Votre projet</span>
        <h2 id="t-c">Parlons de votre jardin</h2>
        <p>Décrivez à Andrei ce que vous souhaitez faire : il vous répond directement.</p>
        <a class="tel2" href="tel:{TELH}">{TEL}</a>
        <div class="actions"><a class="btn btn-sun" href="contact.html">Écrire à Andrei</a><a class="btn btn-line" href="tel:{TELH}">Appeler</a></div>
      </div>
      <div class="stack-img">{img("conception-plan")}</div>
    </div>
  </section>
</main>'''


def realisations():
    return f'''
<main id="contenu">
  <section class="phead bg-sand" aria-labelledby="t-h">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Réalisations</span>
        <h1 id="t-h">Des chantiers réalisés par Andrei</h1>
        <p class="lead">Les photos publiées par Andrei sur sa fiche Google : pelouse, clôture, abri de jardin, dessouchage.</p>
        <div class="actions"><a class="btn btn-ink" href="#galerie">Voir la galerie</a><a class="btn btn-line-dark" href="tel:{TELH}">Appeler Andrei</a></div>
      </div>
      <div class="fan">
        <figure>{img("andrei-cloture-bois", lazy=False)}</figure>
        <figure>{img("andrei-abri-jardin", lazy=False)}</figure>
        <figure>{img("andrei-souche", lazy=False, style="object-position:50% 40%")}</figure>
      </div>
    </div>
  </section>

  <section class="band bg-chalk" id="galerie" aria-labelledby="t-g">
    <div class="wrap">
      <div class="head">
        <span class="eyebrow">Galerie</span>
        <h2 id="t-g">Sur le terrain</h2>
        <p>Photos de chantiers publiées par Andrei sur sa fiche Google.</p>
      </div>
      <div class="gal">
        <figure class="g-a">{img("andrei-pelouse-piscine", style="object-position:50% 55%")}<figcaption class="cap">Pelouse tondue en bandes</figcaption></figure>
        <figure class="g-b">{img("andrei-abri-jardin")}<figcaption class="cap">Abri de jardin en bois</figcaption></figure>
        <figure class="g-c">{img("andrei-cloture-bois")}<figcaption class="cap">Clôture en bois</figcaption></figure>
        <figure class="g-d">{img("andrei-pelouse-terrasse", style="object-position:50% 70%")}<figcaption class="cap">Pelouse au pied d'une terrasse</figcaption></figure>
        <figure class="g-e">{img("andrei-souche", style="object-position:50% 40%")}<figcaption class="cap">Souche arrachée</figcaption></figure>
        <figure class="g-f">{img("andrei-souche-2")}<figcaption class="cap">Terre retournée</figcaption></figure>
      </div>
    </div>
  </section>

  <section class="band bg-palm" aria-labelledby="t-s">
    <div class="wrap">
      <div class="head">
        <span class="eyebrow">Et pour votre jardin ?</span>
        <h2 id="t-s">Ce qu'Andrei peut faire chez vous</h2>
      </div>
      <div class="links3">
        <a class="linkcard" href="services.html#entretenir"><h3>Entretenir</h3><p>Tonte, désherbage, taille de haies, ramassage des feuilles.</p><span class="go">Voir l'entretien →</span></a>
        <a class="linkcard" href="services.html#arbres"><h3>Les arbres</h3><p>Abattage, élagage, arrachage des souches.</p><span class="go">Voir les arbres →</span></a>
        <a class="linkcard" href="services.html#amenager"><h3>Aménager</h3><p>Allées, terrasses, clôtures, abri de jardin.</p><span class="go">Voir l'aménagement →</span></a>
      </div>
    </div>
  </section>

  <section class="band bg-lawn cta2" id="contact" aria-labelledby="t-c">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Un chantier en vue ?</span>
        <h2 id="t-c">Montrez-lui votre jardin</h2>
        <p>Appelez Andrei ou écrivez-lui : il vous répond directement.</p>
        <a class="tel2" href="tel:{TELH}">{TEL}</a>
        <div class="actions"><a class="btn btn-sun" href="contact.html">Écrire à Andrei</a><a class="btn btn-line" href="tel:{TELH}">Appeler</a></div>
      </div>
      <img class="logo-big" src="images/logo-palmier-clair.png" width="300" height="188" alt="" loading="lazy">
    </div>
  </section>
</main>'''


def contact():
    opts = "".join('<option>%s</option>' % o for o in ["Création de massifs ou de pelouse", "Entretien du jardin", "Taille, élagage, abattage", "Aménagement extérieur, petits travaux", "Autre demande"])
    return f'''
<main id="contenu">
  <section class="phead bg-palm" aria-labelledby="t-h">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Contact</span>
        <h1 id="t-h">Parlons de votre jardin</h1>
        <p class="lead">Un besoin, une demande, un projet à réaliser ? Joignez Andrei directement.</p>
        <a class="bigtel" href="tel:{TELH}">{TEL}</a>
        <div class="cinfo"><a href="mailto:{MAIL}">{MAIL}</a><address>{ADR}</address></div>
        <div class="actions"><a class="btn btn-sun" href="tel:{TELH}">Appeler</a><a class="btn btn-line" href="#formulaire">Écrire un message</a></div>
      </div>
      <div class="arch">
        <div class="frame">{img("andrei-pelouse-piscine", lazy=False, style="object-position:50% 55%")}</div>
      </div>
    </div>
  </section>

  <section class="band bg-chalk" id="formulaire" aria-labelledby="t-f">
    <div class="wrap">
      <div class="formcard">
        <h2 id="t-f">Décrivez votre projet</h2>
        <p class="soft" style="margin-top:8px;color:var(--soft)">Préparez votre message ici, puis envoyez-le à Andrei par SMS ou par e-mail. Rien n'est enregistré par ce site.</p>
        <form id="form" novalidate>
          <div class="row2">
            <div class="fld"><label for="f-nom">Votre nom</label><input id="f-nom" name="nom" type="text" autocomplete="name" required><span class="err" id="e-nom" role="alert"></span></div>
            <div class="fld"><label for="f-tel">Votre téléphone</label><input id="f-tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required><span class="err" id="e-tel" role="alert"></span></div>
          </div>
          <div class="row2">
            <div class="fld"><label for="f-mail">Votre e-mail <span class="opt">(facultatif)</span></label><input id="f-mail" name="mail" type="email" autocomplete="email"><span class="err" id="e-mail" role="alert"></span></div>
            <div class="fld"><label for="f-ville">Votre commune <span class="opt">(facultatif)</span></label><input id="f-ville" name="ville" type="text" autocomplete="address-level2"></div>
          </div>
          <div class="fld"><label for="f-sujet">Votre demande</label><select id="f-sujet" name="sujet" required><option value="">Choisir…</option>{opts}</select><span class="err" id="e-sujet" role="alert"></span></div>
          <div class="fld"><label for="f-msg">Votre projet</label><textarea id="f-msg" name="msg" required></textarea><span class="err" id="e-msg" role="alert"></span></div>
          <button class="btn btn-ink btn-submit" type="submit">Préparer mon message</button>
        </form>
        <div class="recap" id="recap" hidden tabindex="-1">
          <h3>Votre message est prêt</h3>
          <pre id="recap-txt"></pre>
          <div class="actions">
            <a class="btn btn-ink" id="r-sms" href="sms:{TELH}">Envoyer par SMS</a>
            <button class="btn btn-ghost" type="button" id="r-copy">Copier</button>
            <a class="btn btn-ghost" href="tel:{TELH}">Appeler</a>
            <a class="btn btn-ghost" id="r-mail" href="mailto:{MAIL}" hidden>Envoyer par e-mail</a>
          </div>
          <p class="note">Le message part depuis votre téléphone ou votre messagerie : choisissez le moyen qui vous convient.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band bg-sun" id="trouver" aria-labelledby="t-t">
    <div class="wrap find">
      <div>
        <span class="eyebrow">Nous trouver</span>
        <h2 id="t-t">Andrei à Andrésy</h2>
        <address>{ADR}</address>
        <div class="actions"><a class="btn btn-ink" href="tel:{TELH}">Appeler {TEL}</a><a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&amp;query=5+chemin+des+Ecoliers+78570+Andresy" target="_blank" rel="noopener">Voir sur la carte</a></div>
      </div>
      <img class="logo-big" src="images/logo-palmier.png" width="300" height="188" alt="" loading="lazy">
    </div>
  </section>
</main>'''


def mentions():
    return f'''
<main id="contenu">
  <section class="phead short bg-palm" aria-labelledby="t-h">
    <div class="wrap">
      <span class="eyebrow">Informations légales</span>
      <h1 id="t-h">Mentions légales</h1>
    </div>
  </section>
  <section class="band bg-chalk" aria-label="Mentions légales">
    <div class="wrap docs">
      <div class="doc"><h2>Éditeur</h2><dl>
        <div><dt>Entreprise</dt><dd>Andrei PINTILII, entrepreneur individuel (Jardinier Andrei)</dd></div>
        <div><dt>SIREN / SIRET</dt><dd>923 150 528 / 923 150 528 00019</dd></div>
        <div><dt>Activité (NAF)</dt><dd>81.30Z, activités d'aménagement paysager</dd></div>
        <div><dt>Adresse</dt><dd>{ADR}</dd></div>
        <div><dt>Téléphone</dt><dd><a href="tel:{TELH}">{TEL}</a></dd></div>
        <div><dt>E-mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
      </dl></div>
      <div class="doc"><h2>Ce site</h2>
        <p>Ce site est une maquette de démonstration, hébergée par GitHub Pages (GitHub, Inc.). L'hébergeur et le directeur de la publication du site définitif seront précisés à sa mise en ligne.</p>
        <h2 style="margin-top:22px">Données personnelles</h2>
        <p>Le formulaire de contact fonctionne dans votre navigateur : aucune donnée n'est envoyée ni enregistrée par ce site, et il n'utilise pas de cookies. Les polices de caractères sont chargées depuis Google Fonts.</p>
        <h2 style="margin-top:22px">Images</h2>
        <p>Les photos de chantiers proviennent de la fiche Google de l'entreprise. Les autres images sont des illustrations génériques, qui ne représentent pas des réalisations de l'entreprise.</p>
      </div>
    </div>
  </section>
</main>'''


SITE = {
    "index.html": ("Jardinier Andrei, paysagiste à Andrésy (78) | Création, entretien, élagage",
                   "Jardinier Andrei, paysagiste à Andrésy (78) : création de massifs et de pelouse, entretien du jardin, taille, élagage, abattage et petits travaux d'aménagement extérieur.", None),
    "services.html": ("Services de jardinage à Andrésy | Jardinier Andrei",
                      "Création de massifs et de pelouse, entretien du jardin, taille de haies, élagage, abattage, arrachage de souches et petits travaux d'aménagement extérieur à Andrésy (78).", services),
    "realisations.html": ("Réalisations | Jardinier Andrei, Andrésy",
                          "Photos de chantiers de Jardinier Andrei à Andrésy : pelouse, clôture en bois, abri de jardin, dessouchage.", realisations),
    "contact.html": ("Contact | Jardinier Andrei, Andrésy (78)",
                     "Contactez Jardinier Andrei à Andrésy : téléphone 06 05 50 79 47, e-mail et formulaire pour préparer votre message par SMS ou par e-mail.", contact),
    "mentions-legales.html": ("Mentions légales | Jardinier Andrei",
                              "Mentions légales de Jardinier Andrei, entrepreneur individuel à Andrésy (78) : identification de l'entreprise, données personnelles, images.", mentions),
}


def page(fn):
    t, d, f = SITE[fn]
    body = home() if f is None else f()
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#173f2a">
<link rel="icon" href="favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="style.css">
</head>
<body>
{header(fn)}
{body}
{footer()}
<script src="script.js"></script>
</body>
</html>
'''


TITLE = "Jardinier Andrei, paysagiste à Andrésy (78) | Création, entretien, élagage"
DESC = "Jardinier Andrei, paysagiste à Andrésy (78) : création de massifs et de pelouse, entretien du jardin, taille, élagage, abattage et petits travaux d'aménagement extérieur."
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,600..800,100&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700;6..12,800&display=swap"

if MODE == "artifact":
    out = os.path.join(os.path.dirname(ROOT), "andrei", "artifact")
    os.makedirs(out, exist_ok=True)
    css = open(os.path.join(ROOT, "style.css"), encoding="utf8").read()
    js = open(os.path.join(ROOT, "script.js"), encoding="utf8").read()
    html = f'''<title>Jardinier Andrei Andrésy</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{DESC}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>
{css}
</style>
{header("index.html")}
{home()}
{footer()}
<script>
{js}
</script>
'''
    open(os.path.join(out, "index.html"), "w", encoding="utf8").write(html)
    print("artefact ok", len(html) // 1024, "Ko")

if MODE == "site":
    for fn in SITE:
        open(os.path.join(ROOT, fn), "w", encoding="utf8").write(page(fn))
    print("site ok", len(SITE), "pages")
