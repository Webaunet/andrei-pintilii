"""Redimensionne et compresse les images du site.
Usage : python3 optimiser_images.py PHOTOS_REELLES GENERIQUES [SORTIE]
  PHOTOS_REELLES : dossier contenant gm1.jpg ... gm8.jpg (photos publiées par le propriétaire sur sa fiche Google)
  GENERIQUES     : dossier d'images génériques du métier
"""
import os, sys
from PIL import Image

REEL, GEN = sys.argv[1], sys.argv[2]
OUT = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
os.makedirs(OUT, exist_ok=True)

# nom de sortie : (dossier, fichier source, largeur max, qualité)
MAP = {
    # photos réelles
    "andrei-pelouse-piscine": (REEL, "gm1.jpg", 900, 80),
    "andrei-pelouse-terrasse": (REEL, "gm3.jpg", 800, 74),
    "andrei-abri-jardin": (REEL, "gm4.jpg", 1000, 78),
    "andrei-souche": (REEL, "gm5.jpg", 1000, 78),
    "andrei-cloture-bois": (REEL, "gm6.jpg", 1000, 78),
    "andrei-souche-2": (REEL, "gm7.jpg", 800, 78),
    # images génériques du métier
    "creation-massifs": (GEN, "4-creation-espace-vert.jpg", 900, 78),
    "entretien-pelouse": (GEN, "2-tonte.jpg", 900, 78),
    "elagage-arbre": (GEN, "1-hero-elagage-chene.jpg", 900, 78),
    "amenagement-terrasse": (GEN, "chantier-terrasse-en-bois.jpg", 900, 78),
    "plantation": (GEN, "6-plantation.jpg", 900, 78),
    "nivellement-terrain": (GEN, "8-nivellement.jpg", 900, 78),
    "taille-haie": (GEN, "4-taille-haies.jpg", 900, 78),
    "desherbage-massif": (GEN, "4-desherbage.jpg", 900, 78),
    "feuilles-mortes": (GEN, "5-feuilles.jpg", 900, 78),
    "dessouchage": (GEN, "3-dessouchage.jpg", 900, 78),
    "maconnerie-pierre": (GEN, "maconerie-paysagere.jpg", 900, 78),
    "allee-dallee": (GEN, "allee-paves-carrelage-exterieure.jpg", 900, 78),
    "conception-plan": (GEN, "conception-chantier.jpg", 900, 78),
    "robot-tonte": (GEN, "robot-tonte-de-pelouse.jpg", 900, 78),
    "jardin-cottage": (GEN, "7-entretien-jardin.jpg", 1400, 76),
}
only = set(a for a in sys.argv[4:])
tot = 0
for name, (d, f, w, q) in MAP.items():
    if only and name not in only:
        continue
    im = Image.open(os.path.join(d, f)).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    p = os.path.join(OUT, name + ".jpg")
    im.save(p, quality=q, optimize=True, progressive=True)
    s = os.path.getsize(p)
    tot += s
    print(f"{name}.jpg {im.size[0]}x{im.size[1]} {s // 1024} Ko")
print("total", tot // 1024, "Ko")
