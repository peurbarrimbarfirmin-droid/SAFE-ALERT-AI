"""
utils.py — SAFE-ALERT-AI
Fonctions utilitaires du dashboard.
"""
import base64, os
import pandas as pd
import numpy as np
import joblib
import streamlit as st
from icons import icon

# ─────────────────────────────────────────────────────────────────────────────
# CHEMINS
# ─────────────────────────────────────────────────────────────────────────────
ROOT       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH  = os.path.join(ROOT, "data", "processed", "alertes_cameroun_final.csv")
MODELS_DIR = os.path.join(ROOT, "models")
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

# ─────────────────────────────────────────────────────────────────────────────
# COULEURS URGENCE
# ─────────────────────────────────────────────────────────────────────────────
URGENCE_CONFIG = {
    "CRITIQUE": {"color": "#E74C3C", "bg": "#FDEDEC", "emoji": "CRIT", "icon": "alert"},
    "ÉLEVÉ":    {"color": "#E67E22", "bg": "#FEF9E7", "emoji": "ELEV", "icon": "alert"},
    "MOYEN":    {"color": "#F39C12", "bg": "#FFFDE7", "emoji": "MOY",  "icon": "bolt"},
    "FAIBLE":   {"color": "#27AE60", "bg": "#EAFAF1", "emoji": "FAIB", "icon": "check"},
}

JOURS_FR    = {"Monday":"Lundi","Tuesday":"Mardi","Wednesday":"Mercredi",
               "Thursday":"Jeudi","Friday":"Vendredi","Saturday":"Samedi","Sunday":"Dimanche"}

# ─────────────────────────────────────────────────────────────────────────────
# CHARGEMENT
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_data
def charger_donnees():
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
    df["Date"]    = pd.to_datetime(df["Date"])
    df["Semaine"] = df["Date"].dt.isocalendar().week.astype(int)
    df["Jour_FR"] = df["Jour_semaine"].map(JOURS_FR)
    return df

@st.cache_resource
def charger_modeles():
    modeles = {}
    fichiers = {
        "rf": "rf_urgence.pkl", "nlp_type": "nlp_pipeline.pkl",
        "nlp_urgence": "nlp_urgence_pipeline.pkl", "le_type": "le_type_incident.pkl",
        "le_ville": "le_ville.pkl", "le_jour": "le_jour.pkl",
        "le_urgence": "le_urgence.pkl", "features_rf": "features_rf.pkl",
    }
    for key, fname in fichiers.items():
        path = os.path.join(MODELS_DIR, fname)
        if os.path.exists(path):
            modeles[key] = joblib.load(path)
    return modeles

def get_bg_base64():
    """Charge l'image de fond en base64 pour l'injecter dans CSS."""
    bg_path = os.path.join(STATIC_DIR, "bg.png")
    if os.path.exists(bg_path):
        with open(bg_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{data}"
    return None

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def get_urgence_style(niveau):
    return URGENCE_CONFIG.get(niveau, {"color": "#95A5A6", "bg": "#F8F9FA", "emoji": "—", "icon": "info"})

def formater_duree(minutes):
    if minutes < 60:
        return f"{int(minutes)} min"
    h = int(minutes // 60); m = int(minutes % 60)
    return f"{h}h {m}min" if m > 0 else f"{h}h"

def get_recommandation(urgence):
    R = {
        "CRITIQUE": "Envoyer les secours immédiatement. Alerter les autorités locales et les services d'urgence.",
        "ÉLEVÉ":    "Intervenir rapidement. Contacter les forces de l'ordre et prévenir les proches.",
        "MOYEN":    "Surveiller la situation. Envoyer une patrouille dans les 30 minutes.",
        "FAIBLE":   "Enregistrer le signalement. Prévoir une vérification dans les prochaines heures.",
    }
    return R.get(urgence, "Analyser la situation.")

def score_danger(urgence):
    return {"CRITIQUE": 0.95, "ÉLEVÉ": 0.72, "MOYEN": 0.45, "FAIBLE": 0.18}.get(urgence, 0.5)

# ─────────────────────────────────────────────────────────────────────────────
# KPI CARD — Version Premium Glassmorphism
# ─────────────────────────────────────────────────────────────────────────────
def kpi_card_html(titre: str, valeur: str, sous_titre: str = "", couleur: str = "#e74c3c", icon_name: str = "chart-bar") -> str:
    ic = icon(icon_name, size=22, color=couleur)
    return f"""
    <div style="
        background: linear-gradient(145deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.03) 100%);
        border: 1px solid rgba(255,255,255,0.1);
        border-top: 3px solid {couleur};
        border-radius: 14px;
        padding: 1.1rem 1.2rem 0.9rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.25), 0 1px 4px rgba(0,0,0,0.15);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        transition: transform .18s ease, box-shadow .18s ease;
        min-height: 108px;
        position: relative; overflow: hidden;
    ">
        <div style="position:absolute; right:-10px; bottom:-10px; opacity:0.06; transform:scale(2.5);">{icon(icon_name, size=40, color=couleur)}</div>
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
            <div style="width:34px; height:34px; border-radius:8px;
                        background:linear-gradient(135deg,{couleur}30,{couleur}18);
                        display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                {ic}
            </div>
            <div style="font-size:0.7rem; font-weight:700; text-transform:uppercase;
                        letter-spacing:0.08em; color:rgba(255,255,255,0.5); line-height:1.2;">{titre}</div>
        </div>
        <div style="font-size:1.85rem; font-weight:800; color:#fff; line-height:1; margin-bottom:4px;">{valeur}</div>
        <div style="font-size:0.72rem; color:rgba(255,255,255,0.4); font-weight:400;">{sous_titre}</div>
    </div>"""

# ─────────────────────────────────────────────────────────────────────────────
# FILTER BAR — Belle barre de filtres Ville / Quartier
# ─────────────────────────────────────────────────────────────────────────────
def filter_dataframe_by_geo(df, tab_id, T):
    """Affiche un filtre bar stylisé et retourne le df filtré."""
    # Conteneur visuel
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1);
                border-radius:12px; padding:0.8rem 1rem 0.4rem; margin-bottom:1rem;
                display:flex; align-items:center; gap:8px;">
        <div style="color:rgba(255,255,255,0.5); flex-shrink:0;">{icon("filter", 16, "rgba(255,255,255,0.5)")}</div>
        <span style="font-size:0.72rem; font-weight:700; text-transform:uppercase;
                     letter-spacing:0.08em; color:rgba(255,255,255,0.4);">Filtres</span>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    villes = [T["filter_all"]] + sorted(df["Ville"].dropna().unique().tolist())
    ville_sel = c1.selectbox(T["filter_city"], villes, key=f"ville_{tab_id}", label_visibility="visible")

    df_v = df[df["Ville"] == ville_sel] if ville_sel != T["filter_all"] else df
    quartiers = [T["filter_all_f"]] + sorted(df_v["Quartier"].dropna().unique().tolist())
    quartier_sel = c2.selectbox(T["filter_neighborhood"], quartiers, key=f"quartier_{tab_id}", label_visibility="visible")

    if quartier_sel != T["filter_all_f"]:
        df_v = df_v[df_v["Quartier"] == quartier_sel]

    return df_v

# ─────────────────────────────────────────────────────────────────────────────
# PREDICTION CARD — Résultat IA
# ─────────────────────────────────────────────────────────────────────────────
def prediction_card_html(type_inc, urgence, score, recommandation, conf_type=95.0, conf_urg=90.0, ressources="Police", temps="15 min"):
    cfg = get_urgence_style(urgence)
    ic_urg = icon(cfg["icon"], size=16, color=cfg["color"])

    bar_pct = int(score * 100)
    bar_color = cfg["color"]

    rows = [
        (icon("tag", 15, "#aaa"),    "Catégorie",          f'<strong style="color:#fff;">{type_inc}</strong> <span style="font-size:11px;color:#888;">({conf_type:.0f}%)</span>'),
        (icon("alert", 15, "#aaa"),  "Urgence",            f'<span style="background:{cfg["color"]}22; color:{cfg["color"]}; padding:2px 10px; border-radius:20px; font-weight:700; font-size:12px; border:1px solid {cfg["color"]}55;">{urgence}</span> <span style="font-size:11px;color:#888;">({conf_urg:.0f}%)</span>'),
        (icon("clock", 15, "#aaa"),  "Délai estimé",       f'<strong style="color:#fff;">{temps}</strong>'),
        (icon("users", 15, "#aaa"),  "Ressources",         f'<span style="color:#ccc;">{ressources}</span>'),
    ]
    rows_html = "".join(f"""
    <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
        <td style="padding:9px 0; color:#888; font-size:12px; white-space:nowrap; width:28px;">{r[0]}</td>
        <td style="padding:9px 8px; color:#888; font-size:12px; width:100px;">{r[1]}</td>
        <td style="padding:9px 0;">{r[2]}</td>
    </tr>""" for r in rows)

    return f"""
    <div style="background:rgba(255,255,255,0.04); border:1px solid {cfg['color']}44;
                border-radius:16px; padding:1.4rem; margin-top:0.5rem;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:1rem;
                    padding-bottom:0.8rem; border-bottom:1px solid rgba(255,255,255,0.08);">
            <div style="width:36px; height:36px; border-radius:8px;
                        background:{cfg['color']}22; border:1px solid {cfg['color']}55;
                        display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                {icon(cfg['icon'], 20, cfg['color'])}
            </div>
            <div>
                <div style="font-size:0.75rem; color:#888; text-transform:uppercase; letter-spacing:.08em;">Résultat de l'analyse IA</div>
                <div style="font-size:1rem; font-weight:700; color:{cfg['color']};">{urgence}</div>
            </div>
        </div>

        <div style="margin-bottom:1rem;">
            <div style="font-size:11px; color:#888; margin-bottom:4px;">Score de danger</div>
            <div style="height:6px; background:rgba(255,255,255,0.08); border-radius:3px; overflow:hidden;">
                <div style="height:100%; width:{bar_pct}%; background:linear-gradient(90deg,{bar_color}88,{bar_color}); border-radius:3px; transition:width 0.5s;"></div>
            </div>
            <div style="font-size:11px; color:{bar_color}; text-align:right; margin-top:2px; font-weight:700;">{bar_pct}%</div>
        </div>

        <table style="width:100%; border-collapse:collapse;">{rows_html}</table>

        <div style="margin-top:1rem; padding:0.8rem; background:rgba(255,255,255,0.04);
                    border-radius:10px; border-left:3px solid {cfg['color']};">
            <div style="font-size:10px; font-weight:700; color:{cfg['color']}; text-transform:uppercase;
                        letter-spacing:.08em; margin-bottom:4px;">Action recommandée</div>
            <div style="font-size:0.82rem; color:#ccc; line-height:1.5;">{recommandation}</div>
        </div>
    </div>"""

def formater_delta(val, reference, inverse=False):
    delta = val - reference
    pct   = (delta / reference * 100) if reference else 0
    fleche = "▲" if delta > 0 else "▼"
    couleur = "#E74C3C" if (delta > 0) != inverse else "#27AE60"
    return fleche, round(pct, 1), couleur
