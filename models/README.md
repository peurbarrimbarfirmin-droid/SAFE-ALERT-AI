# SAFE-ALERT-AI — Modèles entraînés

Ce dossier contient les modèles et artefacts ML sérialisés.

| Fichier | Description |
|---------|-------------|
| `meilleur_modele.pkl` | Modèle principal entraîné |
| `scaler.pkl` | StandardScaler pour la normalisation |
| `features.pkl` | Liste des features sélectionnées |
| `pca.pkl` | ACP pour l'indice de risque |
| `scaler_acp.pkl` | Scaler pour l'ACP |
| `seuils.pkl` | Seuils de classification par zone |
| `seuils_contextuels.pkl` | Seuils contextuels (percentiles p90) |

## Convention

Tous les modèles sont sauvegardés avec `joblib.dump()` et chargés avec `joblib.load()`.
