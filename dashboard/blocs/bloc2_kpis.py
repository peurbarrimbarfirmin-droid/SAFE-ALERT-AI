# SAFE-ALERT-AI — Bloc 2 : KPIs nationaux
import streamlit as st
import pandas as pd


def render_bloc2_kpis(df: pd.DataFrame, lang: str = "fr"):
    """Affiche les indicateurs clés nationaux."""
    titre = "📊 Indicateurs clés" if lang == "fr" else "📊 Key Indicators"
    st.header(titre)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Zones surveillées", "—")
    with col2:
        st.metric("Niveau moyen", "—")
    with col3:
        st.metric("Alertes actives", "—")
    with col4:
        st.metric("Tendance", "—")
