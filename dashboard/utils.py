# SAFE-ALERT-AI — Fonctions utilitaires du dashboard

import pandas as pd
import numpy as np


def charger_donnees(path: str) -> pd.DataFrame:
    """Charge le dataset principal."""
    try:
        if path.endswith(".parquet"):
            return pd.read_parquet(path)
        elif path.endswith(".csv"):
            return pd.read_csv(path)
        else:
            return pd.DataFrame()
    except Exception as e:
        print(f"Erreur chargement données : {e}")
        return pd.DataFrame()


def calculer_indice_risque(df: pd.DataFrame) -> pd.DataFrame:
    """Calcule l'indice de risque pour chaque zone."""
    # À implémenter selon la logique métier du projet
    return df


def get_niveau_alerte(score: float) -> dict:
    """Retourne le niveau d'alerte et la couleur associée."""
    if score < 0.25:
        return {"niveau": "FAIBLE", "couleur": "#27AE60", "emoji": "🟢"}
    elif score < 0.50:
        return {"niveau": "MODÉRÉ", "couleur": "#F39C12", "emoji": "🟡"}
    elif score < 0.75:
        return {"niveau": "ÉLEVÉ", "couleur": "#E67E22", "emoji": "🟠"}
    else:
        return {"niveau": "CRITIQUE", "couleur": "#E74C3C", "emoji": "🔴"}
