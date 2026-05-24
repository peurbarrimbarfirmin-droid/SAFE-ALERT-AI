# SAFE-ALERT-AI — Bloc 5 : Aide à la décision
import streamlit as st
import pandas as pd


def render_bloc5_decision(df: pd.DataFrame, lang: str = "fr"):
    """Affiche le module d'aide à la décision par profil."""
    titre = "🏥 Aide à la décision" if lang == "fr" else "🏥 Decision Support"
    st.header(titre)
    
    profil = st.selectbox(
        "Profil utilisateur" if lang == "fr" else "User Profile",
        ["Citoyen", "Médecin", "Autorité locale", "Chercheur"]
    )
    st.info(f"Recommandations pour le profil **{profil}** — à implémenter.")
