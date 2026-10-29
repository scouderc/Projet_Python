import pandas as pd
from pathlib import Path

# ============================================================
# 1. IMPORT DES BASES PREPAREES
# ============================================================

# Dossier du projet
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# Import des bases
agribalyse = pd.read_csv(DATA_DIR / "agribalyse.csv")
ciqual = pd.read_csv(DATA_DIR / "ciqual_preparee.csv")
print("Agribalyse :", agribalyse.shape)
print("Ciqual :", ciqual.shape)


# ============================================================
# 2. VERIFICATIONS AVANT FUSION
# ============================================================

# Vérification des clés
print("\nNombre de codes AGB uniques :", agribalyse["code_agb"].nunique())
print("Nombre de codes CIQUAL uniques dans Agribalyse :",
      agribalyse["code_ciqual"].nunique())

print("Nombre de codes CIQUAL uniques dans Ciqual :",
      ciqual["alim_code"].nunique())

# La clé Ciqual doit être unique
assert ciqual["alim_code"].is_unique

# Nombre de correspondances
nb_correspondances = agribalyse["code_ciqual"].isin(
    ciqual["alim_code"]
).sum()

print("\nProduits Agribalyse avec correspondance Ciqual :",
      nb_correspondances)

print("Produits Agribalyse sans correspondance Ciqual :",
      len(agribalyse) - nb_correspondances)


# ============================================================
# 3. SELECTION DES VARIABLES
# ============================================================

# Variables Agribalyse : identification
colonnes_identification = [
    "code_agb",
    "code_ciqual",
    "groupe_aliment",
    "sous_groupe_aliment",
    "nom_produit",
    "nom_lci",
    "preparation",
    "dqr"
]

# Variables environnementales
colonnes_environnement = [
    "score_unique_ef",
    "changement_climatique",
    "changement_climatique_agriculture",
    "changement_climatique_transformation",
    "changement_climatique_emballage",
    "changement_climatique_transport",
    "changement_climatique_distribution",
    "changement_climatique_consommation",
    "utilisation_du_sol",
    "epuisement_ressources_eau",
    "particules_fines"
]

# Variables Agribalyse liées à la santé
colonnes_sante_agribalyse = [
    "toxicite_humaine_non_cancerogenes",
    "toxicite_humaine_cancerogenes"
]

# Variables nutritionnelles Ciqual
colonnes_nutrition = [
    "alim_code",
    "Energie, Règlement UE N° 1169 2011 (kcal 100 g)",
    "Protéines, N x facteur de Jones (g 100 g)",
    "Glucides (g 100 g)",
    "Lipides (g 100 g)",
    "Sucres (g 100 g)",
    "Fibres alimentaires (g 100 g)",
    "Sel chlorure de sodium (g 100 g)",
    "Calcium (mg 100 g)",
    "Fer (mg 100 g)",
    "Sodium (mg 100 g)",
    "Vitamine C (mg 100 g)",
    "SAIN",
    "LIM"
]


# ============================================================
# 4. CREATION DES TABLES SELECTIONNEES
# ============================================================

agribalyse_selection = agribalyse[
    colonnes_identification
    + colonnes_environnement
    + colonnes_sante_agribalyse
].copy()

ciqual_selection = ciqual[colonnes_nutrition].copy()


# ============================================================
# 5. FUSION AGRIBYALSE + CIQUAL
# ============================================================

# Agribalyse est la table principale :
# on conserve donc tous les produits Agribalyse.

table_finale = agribalyse_selection.merge(
    ciqual_selection,
    left_on="code_ciqual",
    right_on="alim_code",
    how="left"
)

# alim_code est redondant avec code_ciqual
table_finale = table_finale.drop(columns="alim_code")


# ============================================================
# 6. VERIFICATIONS APRES FUSION
# ============================================================

print("\nDimensions de la base finale :", table_finale.shape)

# La fusion ne doit pas créer de lignes supplémentaires
assert len(table_finale) == len(agribalyse_selection)

# Vérification des doublons sur le code AGB
assert table_finale["code_agb"].is_unique

# Nombre de produits ayant récupéré des informations Ciqual
nb_match_final = table_finale[
    "Energie, Règlement UE N° 1169 2011 (kcal 100 g)"
].notna().sum()

print("Produits avec informations nutritionnelles :", nb_match_final)
print("Produits sans informations nutritionnelles :",
      len(table_finale) - nb_match_final)

print("\nColonnes de la base finale :")
print(table_finale.columns.tolist())

print("\nAperçu de la base finale :")
print(table_finale.head())


# ============================================================
# 7. ENREGISTREMENT
# ============================================================

table_finale.to_csv(
    DATA_DIR / "database.csv",
    index=False
)
print("\nBase finale enregistrée dans data/database.csv")