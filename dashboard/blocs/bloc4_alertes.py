# SAFE-ALERT-AI — Bloc 4 : Alertes
import streamlit as st
import pandas as pd


def render_bloc4_alertes(df: pd.DataFrame, lang: str = "fr"):
    """Affiche le système d'alertes."""
    titre = "🚨 Alertes" if lang == "fr" else "🚨 Alerts"
    st.header(titre)
    st.info("Module d'alertes — à implémenter.")
