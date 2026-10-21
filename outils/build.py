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
      <div class="actions"><a class="btn btn-ink" href="#" data-soon="Réalisations">Voir toutes les réalisations</a></div>
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


TITLE = "Jardinier Andrei, paysagiste à Andrésy (78) | Création, entretien, élagage"
DESC = "Jardinier Andrei, paysagiste à Andrésy (78) : création de massifs et de pelouse, entretien du jardin, taille, élagage, abattage et petits travaux d'aménagement extérieur."
FONTS = "https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Karla:wght@400;500;700;800&display=swap"

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
