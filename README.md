🌾 Finistech : Clearing & Logistics Platform

📌 Présentation du Projet
Finistech est une plateforme intermédiaire innovante conçue pour sécuriser et optimiser la chaîne de valeur agricole en Bretagne. Le projet se positionne comme une chambre de compensation technologique entre les producteurs locaux et les transformateurs industriels.

L'objectif est de répondre à la volatilité des prix des commodities bretonnes (Lait, Porc, Céréales) via des instruments financiers de type Futures/Forwards, tout en gérant les flux logistiques physiques.

🚀 Objectifs Business
Sécurisation du revenu : Permettre aux agriculteurs de fixer un prix de vente à l'avance (Hedging).

Gestion du risque de contrepartie : Agir en tant que garant des transactions (Clearing).

Optimisation Logistique : Réduire les coûts de transport et l'empreinte carbone entre les fermes (Finistère, Morbihan, etc.) et les usines de transformation.

🛠 Stack Technique & Flux de Données
Le projet utilise une architecture modulaire en Python pour traiter les volumes de données :

Ingestion (Big Data Input) : Récupération de bases de données clients via des fichiers Excel (Agriculteurs & Industriels).

Traitement (Analytics) : * Calcul de scores de fiabilité et de risques de crédit.

Analyse des seuils de rentabilité (Break-even points) basés sur les coûts de production.

Visualisation (Dataviz) : Génération de rapports graphiques sur la répartition de la production et les niveaux de risque par département.

📂 Structure du Code
main.py : Point d'entrée et pilotage de l'application.

data_loader.py : Module dédié à l'extraction et au nettoyage des données (Pandas/Openpyxl).

analytics.py : Moteur de calcul financier et algorithmes de scoring de risque.

viz.py : Fonctions de génération de graphiques (Matplotlib/Seaborn).

🏗 Architecture : Programmation Orientée Objet (POO)
Le moteur de Finistech est structuré en classes pour garantir une gestion rigoureuse des flux financiers et logistiques.

Pourquoi ce choix ?

Encapsulation : Chaque entité (Agriculteur, Industriel, Ordre) regroupe ses propres données et sa propre logique de calcul (ex: un objet Agriculteur calcule lui-même son score de risque).

Robustesse : Le carnet d'ordres n'est pas une simple liste, mais un objet OrderBook qui valide l'intégrité de chaque transaction avant enregistrement.

Évolutivité : Permet d'ajouter facilement de nouveaux produits (Lait, Porc, Algues) ou de nouveaux types de contrats sans impacter le reste du code.

Schéma de communication

L'Agriculteur/Industriel instancie un objet Order.

L'OrderBook reçoit l'objet et interroge le module Analytics pour validation.

Le Matching Engine traite les objets Order validés pour créer un Contract.