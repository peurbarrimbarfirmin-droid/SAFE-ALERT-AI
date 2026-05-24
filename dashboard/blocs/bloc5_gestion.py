# SAFE-ALERT-AI — Onglet 5 : Gestion des alertes
import streamlit as st
import pandas as pd
from utils import get_urgence_style, kpi_card_html, filter_dataframe_by_geo
from translations import get_t


def render_bloc5_gestion(df: pd.DataFrame):
    T    = get_t(st.session_state.get("lang", "fr"))
    lang = st.session_state.get("lang", "fr")

    # ── FILTRES GÉOGRAPHIQUES ─────────────────────────────────────────────────
    df_f = filter_dataframe_by_geo(df, "b5", T)
    if df_f.empty:
        st.warning("⚠️ Aucune donnée pour cette sélection.")
        return

    # ── FILTRES THÉMATIQUES ───────────────────────────────────────────────────
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        recherche = st.text_input(T["b5_search"], key="search_b5", label_visibility="visible")
    with fc2:
        statuts = [T["filter_all"]] + sorted(df_f["Statut"].unique().tolist()) if "Statut" in df_f.columns else [T["filter_all"]]
        statut_sel = st.selectbox(T["filter_status"], statuts, key="statut_b5")
    with fc3:
        urgences = [T["filter_all_f"]] + sorted(df_f["Niveau_urgence"].unique().tolist())
        urg_sel  = st.selectbox(T["filter_priority"], urgences, key="urg_b5")

    # Appliquer filtres thématiques
    if "Statut" in df_f.columns and statut_sel != T["filter_all"]:
        df_f = df_f[df_f["Statut"] == statut_sel]
    if urg_sel != T["filter_all_f"]:
        df_f = df_f[df_f["Niveau_urgence"] == urg_sel]
    if recherche:
        r = recherche.lower()
        mask = (
            df_f["ID_alerte"].astype(str).str.lower().str.contains(r) |
            df_f["Type_incident"].str.lower().str.contains(r) |
            df_f["Description"].str.lower().str.contains(r)
        )
        df_f = df_f[mask]

    # ── MINI KPIs ─────────────────────────────────────────────────────────────
    st.markdown("<hr style='opacity:0.15; margin:0.5rem 0;'>", unsafe_allow_html=True)
    mk1, mk2, mk3, mk4 = st.columns(4)
    n = len(df_f)
    n_crit  = len(df_f[df_f["Niveau_urgence"] == "CRITIQUE"])
    n_resol = len(df_f[df_f["Statut"] == "Résolu"]) if "Statut" in df_f.columns else 0
    n_enc   = len(df_f[df_f["Statut"] == "En cours"]) if "Statut" in df_f.columns else 0

    mk1.markdown(kpi_card_html("Résultats" if lang == "fr" else "Results", f"{n}",       "", "#0ea5e9",  "📋"), unsafe_allow_html=True)
    mk2.markdown(kpi_card_html("Critiques" if lang == "fr" else "Critical", f"{n_crit}", "", "#e74c3c",  "🚨"), unsafe_allow_html=True)
    mk3.markdown(kpi_card_html("Résolus"   if lang == "fr" else "Resolved", f"{n_resol}","", "#27ae60",  "✅"), unsafe_allow_html=True)
    mk4.markdown(kpi_card_html("En cours"  if lang == "fr" else "Ongoing",  f"{n_enc}",  "", "#f59e0b",  "⏳"), unsafe_allow_html=True)

    st.markdown("<hr style='opacity:0.15; margin:0.5rem 0;'>", unsafe_allow_html=True)

    # ── TABLEAU PRINCIPAL ─────────────────────────────────────────────────────
    cols_disp = [c for c in ["ID_alerte", "Date", "Heure", "Ville", "Quartier",
                              "Type_incident", "Niveau_urgence", "Statut"] if c in df_f.columns]

    def urgence_color(val):
        cfg = get_urgence_style(val)
        return f"color: {cfg['color']}; font-weight: 700"

    styled = (
        df_f[cols_disp]
        .sort_values(by=["Date", "Heure"] if "Heure" in df_f.columns else ["Date"], ascending=[False, False])
        .style
        .applymap(urgence_color, subset=["Niveau_urgence"] if "Niveau_urgence" in cols_disp else [])
    )
    st.dataframe(styled, use_container_width=True, hide_index=True, height=360)

    # ── DÉTAIL D'UNE ALERTE ───────────────────────────────────────────────────
    st.markdown("<hr style='opacity:0.15; margin:0.8rem 0;'>", unsafe_allow_html=True)
    st.markdown(f"#### {T['b5_details']}")
    st.caption(T["b5_details_desc"])

    ids_dispo = [T["b5_none"]] + df_f["ID_alerte"].astype(str).tolist()
    id_sel    = st.selectbox("ID", ids_dispo, key="id_b5", label_visibility="collapsed")

    if id_sel != T["b5_none"]:
        row = df_f[df_f["ID_alerte"].astype(str) == id_sel]
        if not row.empty:
            alerte = row.iloc[0]
            cfg    = get_urgence_style(alerte["Niveau_urgence"])
            c_info, c_meta = st.columns([1.3, 1])

            with c_info:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,0.05); border-left:5px solid {cfg['color']};
                            border-radius:10px; padding:1rem; margin-top:0.3rem;">
                    <div style="font-size:11px; text-transform:uppercase; letter-spacing:.08em;
                                color:#888; margin-bottom:6px;">
                        {'Description originale' if lang=='fr' else 'Original description'}
                    </div>
                    <div style="font-style:italic; font-size:0.95rem; line-height:1.6;">
                        « {alerte.get('Description', 'N/A')} »
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with c_meta:
                items = [
                    ("🏷️ Type",      alerte.get("Type_incident", "N/A")),
                    ("🚨 Urgence",    f"{cfg['emoji']} {alerte.get('Niveau_urgence','N/A')}"),
                    ("📍 Quartier",  alerte.get("Quartier", "N/A")),
                    ("🏙️ Ville",     alerte.get("Ville", "N/A")),
                    ("📅 Date",      str(alerte.get("Date", "N/A"))[:10]),
                    ("✅ Statut",    alerte.get("Statut", "N/A")),
                ]
                for label, val in items:
                    st.markdown(f"**{label}** : {val}")
