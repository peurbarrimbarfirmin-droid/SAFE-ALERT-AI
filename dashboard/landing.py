# SAFE-ALERT-AI — Landing Page
import streamlit as st


def render_landing():
    """Affiche la page d'accueil / landing page du dashboard."""
    st.markdown("""
    <div style="text-align:center; padding: 3rem 0;">
        <h1 style="font-size:3rem; color:#C0392B;">🛡️ SAFE-ALERT-AI</h1>
        <p style="font-size:1.3rem; color:#555;">
            Système d'alerte précoce et d'aide à la décision
        </p>
    </div>
    """, unsafe_allow_html=True)
