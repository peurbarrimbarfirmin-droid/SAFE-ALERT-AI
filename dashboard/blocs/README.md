# Blocs du Dashboard SAFE-ALERT-AI

## Description

Ce dossier contient les blocs thématiques du dashboard Streamlit.

| Fichier | Contenu |
|---------|---------|
| `bloc1_carte.py` | Carte interactive des zones surveillées |
| `bloc2_kpis.py` | Indicateurs clés (KPIs) nationaux |
| `bloc3_predictions.py` | Prédictions et simulateur |
| `bloc4_alertes.py` | Système d'alertes et notifications |
| `bloc5_decision.py` | Aide à la décision par profil utilisateur |
| `bloc6_profil.py` | Profil contextuel et analyse zonale |

## Convention de nommage

Chaque bloc expose une fonction `render_bloc_N(df, lang)` appelée depuis `app.py`.
