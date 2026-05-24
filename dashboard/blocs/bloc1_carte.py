# SAFE-ALERT-AI — Bloc 1 : Carte interactive
import streamlit as st
import pandas as pd


def render_bloc1_carte(df: pd.DataFrame, lang: str = "fr"):
    """Affiche la carte interactive des zones surveillées."""
    titre = "🗺️ Carte des zones surveillées" if lang == "fr" else "🗺️ Monitored Zones Map"
    st.header(titre)
    st.info("Carte interactive — à implémenter avec Folium.")
