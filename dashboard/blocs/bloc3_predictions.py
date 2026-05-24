# SAFE-ALERT-AI — Bloc 3 : Prédictions
import streamlit as st
import pandas as pd


def render_bloc3_predictions(df: pd.DataFrame, lang: str = "fr"):
    """Affiche les prédictions et le simulateur."""
    titre = "🔮 Prédictions" if lang == "fr" else "🔮 Predictions"
    st.header(titre)
    st.info("Module de prédictions — à implémenter.")
