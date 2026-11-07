# Supervision, Analyse Forensique et Gestion des Incidents (SAFI)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](SAFI_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE SIS589** · Université de Garoua · Faculté des Sciences · Département de Mathématiques et Informatiques · Master Professionnel en Sécurité des Systèmes Informatiques et des Données · 30 heures
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel · contact : maletyon@proton.me · année académique 2026-2027

> *Quand l'écran de rançon s'affiche, l'attaque est déjà vieille ; la seule question est de savoir si quelqu'un l'a vue venir.*

Ce cours est le maillon opérationnel de la sécurité : détecter, investiguer et maîtriser ce qui survient en temps réel. Il couvre la supervision (SOC, SIEM, IDS/IPS, règles de détection), le cadre normatif et juridique de l'incident et de la preuve (ISO/IEC 27035 et 27037, NIST SP 800-86, RFC 3227, lois camerounaises 2010/012, 2010/013 et 2024/017, Conventions de Malabo et de Budapest), l'analyse forensique (disque, mémoire, réseau, chaîne de custody), la réponse à incident (cycle ISO 27035, CSIRT/CERT, renseignement sur la menace, MITRE ATT&CK), et la mesure (OUI/NON/NEK). Un fil théorique parcourt le cours : le Trilemme CRO (Confidentialité, Fiabilité, Opposabilité). L'entreprise fictive LiZbiZ, à Garoua, subit un rançongiciel, suivi à travers les opérations LOGONE, BÉNOUÉ (supervision), FARO (forensique) et MAYO (réponse). Les noms, dates et montants sont fictifs ; les normes et les textes de loi sont cités d'après leur version officielle.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`SAFI_main.pdf`](SAFI_main.pdf) | Traité complet (prologue, six parties, 20 chapitres, annexes) |
| Les présentations | [`Présentation/`](Présentation/) | 16 présentations : vision d'ensemble et 15 séances de 2 heures |
| Les fiches d'exercices | [`fiches/`](fiches/) | 21 fiches de 40 questions, une par chapitre (prologue compris) |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, [`Style_SAFI.sty`](Style_SAFI.sty) | Sources du livre |

## Organisation du cours (30 heures, 15 séances de 2 heures)

| Partie | Chapitres | Fichiers |
|---|---|---|
| **Prologue** | La découverte | [`partie0/`](partie0/) |
| **I. Superviser** | 1. Pourquoi superviser · 2. L'architecture d'un SOC · 3. Gouvernance et indicateurs | [`partie1/`](partie1/) |
| **II. Collecter et détecter** | 4. Les journaux · 5. Le SIEM · 6. IDS/IPS · 7. Écrire une règle de détection | [`partie2/`](partie2/) |
| **III. Cadre normatif et juridique** | 8. Normes de l'incident et de la preuve · 9. Le cadre juridique · 10. L'admissibilité de la preuve | [`partie3/`](partie3/) |
| **IV. L'analyse forensique** | 11. Fondements et chaîne de custody · 12. Forensique système · 13. Forensique mémoire · 14. Forensique réseau | [`partie4/`](partie4/) |
| **V. La réponse à incident** | 15. Le cycle de réponse · 16. CSIRT et CERT · 17. Renseignement sur la menace · 18. Confiner, éradiquer, rétablir | [`partie5/`](partie5/) |
| **VI. Apprendre et mesurer** | 19. Retour d'expérience · 20. Mesurer la supervision et la réponse | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles · D. Textes · E. Bibliographie commentée · F. Contacts | [`annexes/`](annexes/) |

Chaque chapitre compte dix exercices gradués ; leurs corrigés, et ceux des fiches, sont dans le livret de correction. Les fiches et les labs se font hors des 30 heures.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement compagnon du cours : une fiche d'auto-évaluation de 40 questions par chapitre, corrigée automatiquement, des labs sur pièces et un tableau de bord de progression. Le code de cours est **SIS589**.

> **NDAP SUKULU en local.** La version téléchargeable et installable sur votre poste, avec un module autonome pour ce cours, est en cours de finalisation. En attendant, les fiches d'auto-évaluation de chaque chapitre (40 questions) sont fournies au format texte dans [`fiches/`](fiches/).

| Lab | Chapitre | Sujet |
|---|---|---|
| SAFI-LAB-01 | 3 | Lire un tableau de bord de supervision |
| SAFI-LAB-02 | 4 | Journaux et angles morts |
| SAFI-LAB-03 | 7 | Écrire et éprouver une règle de détection |
| SAFI-LAB-04 | 5 | Reconnaître une intrusion (alertes corrélées) |
| SAFI-LAB-05 | 11 | Chaîne de custody et artefacts |
| SAFI-LAB-06 | 12 | Forensique système : chronologie |
| SAFI-LAB-07 | 14 | Forensique réseau : exfiltration et pilotage |
| SAFI-LAB-08 | 15 | Classer et traiter des incidents |
| SAFI-LAB-09 | 17 | Mapping d'un incident à ATT&CK |
| SAFI-LAB-10 | 20 | Couverture de détection et OUI/NON/NEK |

Tous les labs se pratiquent sur pièces (journaux, images, flux exportés) en environnement fermé.

## Compiler le livre

Avec une distribution LaTeX : `pdflatex SAFI_main`, `biber SAFI_main`, `makeindex SAFI_main`, puis deux fois `pdflatex SAFI_main`.
Les présentations se régénèrent avec `python Présentation/_sources/gen_specs.py` puis `python Présentation/_sources/run.py SAFI all` (Python 3 et python-pptx).

## Les trois cours de l'Université de Garoua

Ce cours fait partie d'un corpus de trois UE du Master SSID : Supervision, Analyse Forensique et Gestion des Incidents (SIS589), Forensique Numérique ([LPI342](https://github.com/maletyon/cours-forn)), Systèmes de Gestion de la Sécurité Informatique ([IS498](https://github.com/maletyon/cours-sgsi)).
