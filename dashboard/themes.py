"""
themes.py — SAFE-ALERT-AI
Deux thèmes complets : Sombre (navy) et Clair.
"""

THEMES = {
    "dark": {
        "bg_primary":   "#020c18", "bg_secondary": "#051525",
        "bg_tertiary":  "#071e35", "bg_elevated":  "#0a2845",
        "bg_card":      "#0d2f50", "text": "#e0f2fe",
        "text2":        "#7fb8d4", "text3": "#3d6b8a",
        "border_soft":  "rgba(14,165,233,0.12)", "border_med": "rgba(14,165,233,0.25)",
        "border_teal":  "rgba(231,76,60,0.20)",
        "sidebar_bg":   "linear-gradient(180deg,#020c18 0%,#051525 100%)",
        "bg_image_overlay": "linear-gradient(145deg,rgba(2,12,24,0.92) 0%,rgba(3,17,31,0.88) 50%,rgba(5,25,41,0.86) 100%)",
    },
    "light": {
        "bg_primary":   "#e8f4fd", "bg_secondary": "#d4ebf8",
        "bg_tertiary":  "#ffffff", "bg_elevated":  "#ffffff",
        "bg_card":      "#f8fbff", "text": "#0a1f33",
        "text2":        "#1a4a6e", "text3": "#3a7ca8",
        "border_soft":  "rgba(10,60,120,0.12)", "border_med": "rgba(10,60,120,0.25)",
        "border_teal":  "rgba(231,76,60,0.25)",
        "sidebar_bg":   "linear-gradient(180deg,#d4ebf8 0%,#e8f4fd 100%)",
        "bg_image_overlay": "linear-gradient(145deg,rgba(200,230,250,0.92) 0%,rgba(180,215,245,0.88) 100%)",
    },
}

ACCENT = {"teal": "#00d4b1", "blue": "#0ea5e9", "amber": "#f59e0b",
          "red": "#e74c3c", "coral": "#f97316", "green": "#27ae60"}

def get_theme(name="dark"):
    th = dict(THEMES.get(name, THEMES["dark"]))
    th.update(ACCENT); th["name"] = name
    return th


def build_css(th: dict, img_data_uri: str) -> str:
    # Si image locale disponible, l'utiliser, sinon fallback gradient
    if img_data_uri:
        bg_css = f'url("{img_data_uri}")'
    else:
        bg_css = "linear-gradient(145deg, #020c18 0%, #051525 40%, #071e35 100%)"

    dark = th["name"] == "dark"
    opt_bg   = "#071e35" if dark else "#ffffff"
    opt_text = "#c8e8f8" if dark else "#0a1f33"
    opt_hover_bg   = "rgba(0,212,177,0.12)" if dark else "rgba(10,60,120,0.08)"
    opt_hover_text = "#00d4b1" if dark else "#002a4e"
    opt_sel_bg     = "rgba(0,212,177,0.08)" if dark else "rgba(10,60,120,0.06)"

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    [data-testid="stHeader"] {{ background: transparent !important; }}
    footer, #MainMenu, .stAppDeployButton {{ display: none !important; }}

    html, body, .stApp {{ font-family: 'Inter', sans-serif; color: {th['text']}; }}

    /* ── FOND ── */
    .stApp {{
        background-image: {bg_css};
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: ''; position: fixed; inset: 0;
        background: {th['bg_image_overlay']};
        z-index: 0; pointer-events: none;
    }}
    .block-container  {{ position: relative; z-index: 1; padding-top: 1.5rem !important; }}
    section[data-testid="stSidebar"] {{ position: relative; z-index: 2; }}

    /* ── SIDEBAR ── */
    section[data-testid="stSidebar"] {{
        background: {th['sidebar_bg']} !important;
        border-right: 1px solid {th['border_teal']} !important;
    }}

    /* ── ONGLETS ── */
    .stTabs [data-baseweb="tab-list"] {{
        background: rgba(255,255,255,0.03) !important;
        border-bottom: 1px solid {th['border_soft']};
        padding: 6px 16px 0; border-radius: 12px 12px 0 0; gap: 6px;
    }}
    .stTabs [data-baseweb="tab"] {{
        font-family: 'Inter', sans-serif !important;
        font-size: 11.5px !important; font-weight: 700 !important;
        text-transform: uppercase !important; letter-spacing: 0.07em !important;
        padding: 10px 16px !important; border-radius: 8px 8px 0 0 !important;
        transition: all .2s ease !important; color: {th['text2']} !important;
        background: transparent !important;
    }}
    .stTabs [aria-selected="true"] {{
        background: rgba(231,76,60,0.08) !important;
        border-bottom: 3px solid #e74c3c !important;
        color: #e74c3c !important;
    }}

    /* ── TEXTES ── */
    p, div, h1, h2, h3, h4, label, span {{ color: {th['text']} !important; }}

    /* ── METRICS ── */
    [data-testid="stMetricValue"] {{ color: #fff !important; font-weight: 800 !important; }}
    [data-testid="stMetricLabel"] {{ color: rgba(255,255,255,0.6) !important; }}

    /* ── INPUTS ── */
    [data-baseweb="input"] > div, textarea, [data-baseweb="textarea"] > div {{
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid {th['border_med']} !important;
        border-radius: 10px !important; color: {th['text']} !important;
    }}

    /* ── SELECTBOXES ── */
    [data-baseweb="select"] > div:first-child {{
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid {th['border_med']} !important;
        border-radius: 10px !important;
    }}
    [data-baseweb="select"] span {{ color: {th['text']} !important; }}

    /* ── DROPDOWN MENUS ── */
    [data-baseweb="popover"] > div,
    [data-baseweb="menu"], ul[role="listbox"], div[role="listbox"] {{
        background-color: {opt_bg} !important;
        border: 1px solid {th['border_med']} !important;
        border-radius: 12px !important;
        box-shadow: 0 16px 48px rgba(0,0,0,0.4) !important;
    }}
    [role="option"], [data-baseweb="menu"] li {{
        background-color: {opt_bg} !important;
        color: {opt_text} !important;
        font-size: 13px !important; font-family: 'Inter', sans-serif !important;
    }}
    [role="option"] span, [role="option"] div, [role="option"] p {{
        color: {opt_text} !important; background-color: transparent !important;
    }}
    [role="option"]:hover, [data-baseweb="menu"] li:hover {{
        background-color: {opt_hover_bg} !important;
    }}
    [role="option"]:hover span, [role="option"]:hover div {{ color: {opt_hover_text} !important; }}
    [aria-selected="true"] {{
        background-color: {opt_sel_bg} !important;
        color: {opt_hover_text} !important; font-weight: 600 !important;
    }}
    [aria-selected="true"] span, [aria-selected="true"] div {{ color: {opt_hover_text} !important; }}

    /* ── DATE INPUTS ── */
    [data-baseweb="calendar"], [data-baseweb="datepicker"] {{
        background: {opt_bg} !important;
        border: 1px solid {th['border_med']} !important; border-radius: 12px !important;
    }}
    [data-testid="stDateInput"] > div {{
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid {th['border_med']} !important; border-radius: 10px !important;
    }}

    /* ── BUTTONS ── */
    [data-testid="baseButton-primary"] {{
        background: linear-gradient(135deg, #e74c3c, #c0392b) !important;
        border: none !important; border-radius: 10px !important;
        font-weight: 700 !important; letter-spacing: 0.04em !important;
        box-shadow: 0 4px 16px rgba(231,76,60,0.35) !important;
        transition: all .2s ease !important;
    }}
    [data-testid="baseButton-primary"]:hover {{
        box-shadow: 0 6px 22px rgba(231,76,60,0.55) !important;
        transform: translateY(-1px) !important;
    }}

    /* ── DATAFRAME ── */
    [data-testid="stDataFrame"] iframe {{ border-radius: 12px !important; }}

    /* ── HR ── */
    hr {{ border-color: {th['border_soft']} !important; opacity: 1 !important; }}

    /* ── SIDEBAR TEXT ── */
    section[data-testid="stSidebar"] label {{ color: {th['text2']} !important; font-size: 11px !important; }}
    section[data-testid="stSidebar"] span  {{ color: {th['text']} !important; }}
    section[data-testid="stSidebar"] [data-baseweb="select"] > div:first-child {{
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid {th['border_med']} !important;
    }}

    /* Collapse button */
    [data-testid="collapsedControl"] svg {{ fill: #FFFFFF !important; color: #FFFFFF !important; }}

    /* ── SPINNER ── */
    [data-testid="stSpinner"] {{ color: #e74c3c !important; }}

    svg text {{ fill: {th['text']} !important; }}
    </style>
    """
