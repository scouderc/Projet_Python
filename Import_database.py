import pandas as pd


# ============================================================
# 1. IMPORT DES BASES
# ============================================================

# Agribalyse - Synthèse
url_agribalyse_synthese = (
    "https://data.ademe.fr/data-fair/api/v1/datasets/"
    "agribalyse-31-synthese/lines?size=10000&format=csv"
)
agribalyse_synthese = pd.read_csv(url_agribalyse_synthese)


# Agribalyse - Détail par étape
url_agribalyse_detail = (
    "https://data.ademe.fr/data-fair/api/v1/datasets/"
    "agribalyse-31-detail-par-etape/lines?size=10000&format=csv"
)
agribalyse_detail_etapes = pd.read_csv(url_agribalyse_detail)


# Ciqual
url_ciqual = (
    "https://ciqual.anses.fr/cms/sites/default/files/inline-files/"
    "Table%20Ciqual%202025_FR_2025_11_03.xlsx"
)
ciqual = pd.read_excel(url_ciqual)


# ============================================================
# 2. VERIFICATION RAPIDE
# ============================================================

print("Agribalyse - Synthèse :", agribalyse_synthese.shape)
print(agribalyse_synthese.head())

print("\nAgribalyse - Détail par étape :", agribalyse_detail_etapes.shape)
print(agribalyse_detail_etapes.head())

print("\nCiqual :", ciqual.shape)
print(ciqual.head())


# ============================================================
# 3. CONTROLES ESSENTIELS
# ============================================================

assert len(agribalyse_synthese) > 0
assert len(agribalyse_detail_etapes) > 0
assert len(ciqual) > 0

assert "Code AGB" in agribalyse_synthese.columns
assert "Code CIQUAL" in agribalyse_synthese.columns