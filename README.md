# 1. Introduction
- (À rédiger : contexte sanitaire et environnemental, enjeux liés à l’alimentation, pollution et intérêt de croiser les dimensions environnementale et nutritionnelle.)

# 2. Présentation des bases de données
- (À rédiger : présentation rapide d’Agribalyse et de Ciqual, leur rôle respectif et les informations qu’elles contiennent.)

# 3. Démarche à suivre pour utiliser le projet
- Installer les logiciels et bibliothèques nécessaires
  - Ouvrir un terminal dans le dossier du projet Python.
  - Installer les bibliothèques nécessaires à l’aide du fichier requirements.txt avec la commande "pip install -r requirements.txt"
- Importer les bases de données
  - Ouvrir et exécuter le programme Import_database.py.
  - Ce programme permet de récupérer automatiquement les trois tables nécessaires depuis les sites de l’ADEME (Agribalyse) et de l’ANSES (Ciqual).
  - Cas particulier : la base Ciqual pouvant être temporairement inaccessible en raison d’une maintenance du site, l’exécution du programme peut générer un message d’erreur lors du téléchargement de cette base. Dans ce cas, placer dans le dossier data/ le fichier Ciqual fourni avec le projet sur GitHub, puis poursuivre les étapes suivantes.
- Préparer et explorer les bases de données
  - Ouvrir et exécuter Exploration_nettoyage_Agribalyse.ipynb.
  - Ouvrir et exécuter Exploration_nettoyage_Ciqual.ipynb.
  - Lire les explications fournies dans les notebooks afin de comprendre les différentes étapes de nettoyage, de transformation et de création des nouvelles variables.
- Créer la base de données finale
  - Exécuter le programme Fusion_BD.py.
  - Ce programme fusionne les données Agribalyse et Ciqual afin de créer la base de données finale database.csv.
- Réaliser et consulter les analyses
  - Ouvrir le notebook Analyse.ipynb.
  - Exécuter les différentes cellules afin d’obtenir les analyses et visualisations réalisées à partir de la base de données finale.