"""Construit les présentations : python run.py SAFI 1 3 5   (ou: python run.py SAFI all)."""
import sys, os, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slides import Deck
from courses import ALL

LABS = {
    "SAFI": {
        "LAB-01": "Lire un tableau de bord de supervision",
        "LAB-02": "Journaux et angles morts",
        "LAB-03": "Écrire et éprouver une règle de détection",
        "LAB-04": "Reconnaître une intrusion (alertes corrélées)",
        "LAB-05": "Chaîne de custody et artefacts",
        "LAB-06": "Forensique système : chronologie",
        "LAB-07": "Forensique réseau : exfiltration et pilotage",
        "LAB-08": "Classer et traiter des incidents",
        "LAB-09": "Mapping d'un incident à ATT&CK",
        "LAB-10": "Couverture de détection et OUI/NON/NEK",
    },
}

HERE = os.path.dirname(os.path.abspath(__file__))


def load(sigle, name):
    path = os.path.join(HERE, "specs", sigle, name + ".py")
    spec = importlib.util.spec_from_file_location(f"{sigle}_{name}", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SPEC


def complete(sigle, day, spec):
    c = ALL[sigle]
    theme, contenu, ateliers, labs = c["jours"][day]
    for d in spec:
        if d["k"] == "maison":
            d.setdefault("ateliers", [f"**Atelier {a[:3]}** : fiche {sigle}-FICHE-{a[:3]}" for a in ateliers])
            d.setdefault("labs", [f"**{sigle}-{l}** : {LABS[sigle][l]}" for l in labs])
    return spec


def build_day(sigle, day):
    c = ALL[sigle]
    spec = complete(sigle, day, load(sigle, f"J{day:02d}"))
    deck = Deck(c, day)
    out = os.path.join(c["dossier"], f"{sigle}_J{day:02d}.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


def build_global(sigle):
    c = ALL[sigle]
    spec = load(sigle, "J00")
    deck = Deck(c, None)
    out = os.path.join(c["dossier"], f"{sigle}_00_vision_globale.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


if __name__ == "__main__":
    sigle = sys.argv[1]
    days = sys.argv[2:]
    if days == ["all"]:
        days = ["0"] + [str(i) for i in range(1, ALL[sigle].get("n_jours", 15) + 1)]
    for dd in days:
        if int(dd) == 0:
            build_global(sigle)
        else:
            build_day(sigle, int(dd))
