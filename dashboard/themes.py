# SAFE-ALERT-AI — Thèmes et styles CSS

THEME_SAFE_ALERT = {
    "primary": "#C0392B",
    "secondary": "#E74C3C",
    "background": "#FFFFFF",
    "secondary_background": "#FFF5F5",
    "text": "#2C3E50",
    "success": "#27AE60",
    "warning": "#F39C12",
    "danger": "#E74C3C",
}

CSS_GLOBAL = """
<style>
    .stApp { font-family: 'Inter', sans-serif; }
    .kpi-card {
        background: linear-gradient(135deg, #C0392B11, #E74C3C22);
        border-radius: 12px;
        padding: 1.2rem;
        border-left: 4px solid #C0392B;
        margin-bottom: 1rem;
    }
    .alert-critique { background-color: #FDEDEC; border-left: 4px solid #E74C3C; }
    .alert-eleve    { background-color: #FEF9E7; border-left: 4px solid #F39C12; }
    .alert-modere   { background-color: #FFF3E0; border-left: 4px solid #E67E22; }
    .alert-faible   { background-color: #EAFAF1; border-left: 4px solid #27AE60; }
</style>
"""


def inject_css():
    """Injecte le CSS global dans Streamlit."""
    import streamlit as st
    st.markdown(CSS_GLOBAL, unsafe_allow_html=True)
