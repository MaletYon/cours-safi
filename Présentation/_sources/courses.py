"""Métadonnées du cours SAFI (SIS589, Université de Garoua) et répartition des
15 séances de 2 heures (30 heures)."""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

SAFI = {
    "sigle": "SAFI",
    "code": "SIS589",
    "titre": "Supervision, Analyse Forensique et Gestion des Incidents",
    "sous_titre": "Détecter, investiguer, maîtriser : du SOC à la preuve opposable",
    "master": "Master Professionnel en Sécurité des Systèmes Informatiques et des Données",
    "bandeau": "Université de Garoua",
    "ecole": "Faculté des Sciences",
    "logo_g": "garoua",
    "logo_d": "garoua",
    "n_jours": 15,
    "annee": "2026-2027",
    "dossier": COURS + r"\UG-DMI\SIS589\Présentation",
    "fil_rouge": "LOGONE, BÉNOUÉ, FARO, MAYO",
    "parties": [
        ("Prologue", "La découverte", "P00"),
        ("Partie I", "Superviser", "C01-C03"),
        ("Partie II", "Collecter et détecter", "C04-C07"),
        ("Partie III", "Cadre normatif et juridique", "C08-C10"),
        ("Partie IV", "L'analyse forensique", "C11-C14"),
        ("Partie V", "La réponse à incident", "C15-C18"),
        ("Partie VI", "Apprendre et mesurer", "C19-C20"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · La découverte", "Présentation du cours + Prologue", ["P00"], []),
        2: ("Pourquoi superviser", "C01", ["C01"], []),
        3: ("L'architecture d'un SOC", "C02", ["C02"], []),
        4: ("Gouvernance, indicateurs · Les journaux", "C03 + C04", ["C03", "C04"], ["LAB-01", "LAB-02"]),
        5: ("Le SIEM · La détection d'intrusion", "C05 + C06", ["C05", "C06"], ["LAB-04"]),
        6: ("Écrire et éprouver une règle de détection", "C07", ["C07"], ["LAB-03"]),
        7: ("Normes de l'incident et de la preuve · Droit", "C08 + C09", ["C08", "C09"], []),
        8: ("Admissibilité · Fondements du forensique", "C10 + C11", ["C10", "C11"], ["LAB-05"]),
        9: ("Forensique système", "C12", ["C12"], ["LAB-06"]),
        10: ("Forensique mémoire", "C13", ["C13"], []),
        11: ("Forensique réseau", "C14", ["C14"], ["LAB-07"]),
        12: ("Le cycle de réponse · CSIRT et CERT", "C15 + C16", ["C15", "C16"], ["LAB-08"]),
        13: ("Renseignement sur la menace · Confiner, éradiquer, rétablir", "C17 + C18", ["C17", "C18"], ["LAB-09"]),
        14: ("Retour d'expérience et amélioration continue", "C19", ["C19"], []),
        15: ("Mesurer la supervision et la réponse · clôture", "C20", ["C20"], ["LAB-10"]),
    },
}

ALL = {"SAFI": SAFI}
