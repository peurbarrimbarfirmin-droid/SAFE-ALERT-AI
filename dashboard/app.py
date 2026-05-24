"""
app.py — SAFE-ALERT-AI
Dashboard principal.
"""
import sys, os
import streamlit as st

_dashboard_dir = os.path.dirname(os.path.abspath(__file__))
if _dashboard_dir not in sys.path:
    sys.path.insert(0, _dashboard_dir)

from utils import charger_donnees, charger_modeles, get_bg_base64
from themes import get_theme, build_css
from translations import get_t
from icons import icon

st.set_page_config(
    page_title="SAFE-ALERT-AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── SESSION ────────────────────────────────────────────────────────────────
if "theme_name" not in st.session_state: st.session_state["theme_name"] = "dark"
if "lang"       not in st.session_state: st.session_state["lang"]       = "fr"

th = get_theme(st.session_state["theme_name"])
T  = get_t(st.session_state["lang"])

# ── DATA & MODELS ──────────────────────────────────────────────────────────
try:
    df      = charger_donnees()
    modeles = charger_modeles()
except Exception as e:
    st.error(f"Données manquantes — exécutez generate_data.py d'abord.\n\n{e}")
    st.stop()

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

# ── CSS ────────────────────────────────────────────────────────────────────
bg_uri = get_bg_base64()
st.markdown(build_css(th, bg_uri), unsafe_allow_html=True)

# Traduction des onglets via CSS (texte fantôme)
st.markdown(f"""
<style>
.stTabs [data-baseweb="tab"] div[data-testid="stMarkdownContainer"] {{ display:none !important; }}
.stTabs [data-baseweb="tab"]:nth-child(1)::after {{ content:"{T['tab_generale']}"; font-family:'Inter',sans-serif; font-size:11.5px; font-weight:700; text-transform:uppercase; letter-spacing:.07em; }}
.stTabs [data-baseweb="tab"]:nth-child(2)::after {{ content:"{T['tab_geo']}"; font-family:'Inter',sans-serif; font-size:11.5px; font-weight:700; text-transform:uppercase; letter-spacing:.07em; }}
.stTabs [data-baseweb="tab"]:nth-child(3)::after {{ content:"{T['tab_ia']}"; font-family:'Inter',sans-serif; font-size:11.5px; font-weight:700; text-transform:uppercase; letter-spacing:.07em; }}
.stTabs [data-baseweb="tab"]:nth-child(4)::after {{ content:"{T['tab_stats']}"; font-family:'Inter',sans-serif; font-size:11.5px; font-weight:700; text-transform:uppercase; letter-spacing:.07em; }}
.stTabs [data-baseweb="tab"]:nth-child(5)::after {{ content:"{T['tab_gestion']}"; font-family:'Inter',sans-serif; font-size:11.5px; font-weight:700; text-transform:uppercase; letter-spacing:.07em; }}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ────────────────────────────────────────────────────────────────
with st.sidebar:
    # Header visuel
    st.markdown(f"""
    <div style="padding:1.2rem 0.8rem 1rem; text-align:center;">
        <div style="width:56px; height:56px; border-radius:14px;
                    background:linear-gradient(135deg,#e74c3c22,#e74c3c11);
                    border:1.5px solid #e74c3c44;
                    display:flex; align-items:center; justify-content:center;
                    margin:0 auto 10px;">
            <span style="color:#e74c3c;">{icon("shield", 28, "#e74c3c")}</span>
        </div>
        <div style="font-size:1.15rem; font-weight:900; color:#fff; letter-spacing:.04em;">SAFE ALERT AI</div>
        <div style="font-size:9px; font-weight:700; color:#e74c3c; letter-spacing:.14em; margin-top:3px;">
            {T['sidebar_app_subtitle']}
        </div>
    </div>
    <div style="height:1px; background:linear-gradient(90deg,transparent,rgba(231,76,60,0.4),transparent); margin:0 0 1rem;"></div>
    """, unsafe_allow_html=True)

    # Thème / Langue
    st.markdown(f"<div style='font-size:10px; font-weight:700; color:{th['text3']}; text-transform:uppercase; letter-spacing:.08em; margin-bottom:6px;'>{T['sidebar_theme_title']} & {T['sidebar_lang_title']}</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    def upd_th(): st.session_state["theme_name"] = "dark" if "Dark" in st.session_state.sb_th or "Sombre" in st.session_state.sb_th else "light"
    def upd_lg(): st.session_state["lang"] = "fr" if "FR" in st.session_state.sb_lg else "en"

    idx_th = 0 if st.session_state["theme_name"] == "dark" else 1
    idx_lg = 0 if st.session_state["lang"] == "fr" else 1
    c1.selectbox("T", [f"Sombre", "Clair"], index=idx_th, key="sb_th", on_change=upd_th, label_visibility="collapsed")
    c2.selectbox("L", ["FR", "EN"], index=idx_lg, key="sb_lg", on_change=upd_lg, label_visibility="collapsed")

    st.markdown("<div style='height:1px; background:rgba(255,255,255,0.08); margin:1rem 0;'></div>", unsafe_allow_html=True)

    # Dates
    st.markdown(f"<div style='font-size:10px; font-weight:700; color:{th['text3']}; text-transform:uppercase; letter-spacing:.08em; margin-bottom:6px;'>{T['sidebar_period_label']}</div>", unsafe_allow_html=True)
    dc1, dc2 = st.columns(2)
    date_start = dc1.date_input(T["sidebar_date_start"], min_date, min_value=min_date, max_value=max_date, label_visibility="visible")
    date_end   = dc2.date_input(T["sidebar_date_end"],   max_date, min_value=min_date, max_value=max_date, label_visibility="visible")

    st.markdown("<div style='height:60px;'></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:9.5px; color:{th['text3']}; text-align:center;'>© 2026 SAFE-ALERT-AI</div>", unsafe_allow_html=True)

# ── FILTRE DATES ────────────────────────────────────────────────────────────
df_filtered = df[(df["Date"].dt.date >= date_start) & (df["Date"].dt.date <= date_end)]

# ── ONGLETS ─────────────────────────────────────────────────────────────────
from blocs.bloc1_vue_generale import render_bloc1_vue_generale
from blocs.bloc2_geographie   import render_bloc2_geographie
from blocs.bloc3_ia_nlp       import render_bloc3_ia
from blocs.bloc4_statistiques import render_bloc4_statistiques
from blocs.bloc5_gestion      import render_bloc5_gestion

tabs = st.tabs(["0", "1", "2", "3", "4"])
with tabs[0]: render_bloc1_vue_generale(df_filtered)
with tabs[1]: render_bloc2_geographie(df_filtered)
with tabs[2]: render_bloc3_ia(df_filtered, modeles)
with tabs[3]: render_bloc4_statistiques(df_filtered)
with tabs[4]: render_bloc5_gestion(df_filtered)
