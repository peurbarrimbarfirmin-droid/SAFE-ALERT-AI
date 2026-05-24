# SAFE-ALERT-AI — Onglet 2 : Analyse Géographique & Heatmap
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from utils import kpi_card_html, filter_dataframe_by_geo
from translations import get_t
from icons import icon


def render_bloc2_geographie(df: pd.DataFrame):
    T = get_t(st.session_state.get("lang", "fr"))

    # ── FILTRES ───────────────────────────────────────────────────────────────
    df_f = filter_dataframe_by_geo(df, "b2", T)
    if df_f.empty:
        st.warning("⚠️ Aucune donnée pour cette sélection.")
        return

    # ── KPIs GÉOGRAPHIQUES ───────────────────────────────────────────────────
    top_quartier = df_f["Quartier"].value_counts().index[0] if len(df_f) > 0 else "N/A"
    nb_quartiers = df_f["Quartier"].nunique()
    nb_villes    = df_f["Ville"].nunique()
    nb_regions   = df_f["Region"].nunique() if "Region" in df_f.columns else "—"
    temps_moy    = df_f["Temps_intervention_minutes"].mean() if "Temps_intervention_minutes" in df_f.columns else 45

    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(kpi_card_html(T["b2_kpi_quartier"], top_quartier,           "🏘️ Zone la plus touchée",           "#e74c3c", "📍"), unsafe_allow_html=True)
    k2.markdown(kpi_card_html(T["b2_kpi_zones"],    f"{nb_quartiers} qtrs / {nb_villes} villes", "Zones actives", "#0ea5e9", "🗺️"), unsafe_allow_html=True)
    k3.markdown(kpi_card_html(T["b2_kpi_temps"],    f"{int(temps_moy)} min", "Toutes zones confondues",          "#f59e0b", "⏱️"), unsafe_allow_html=True)
    k4.markdown(kpi_card_html("Régions",             str(nb_regions),         "Régions actives",                  "#27ae60", "🌍"), unsafe_allow_html=True)

    st.markdown("<hr style='opacity:0.15; margin:1rem 0;'>", unsafe_allow_html=True)

    # ── CARTE HEATMAP + TOP QUARTIERS ─────────────────────────────────────────
    col_map, col_chart = st.columns([1.4, 1], gap="large")

    with col_map:
        if "Latitude" in df_f.columns and "Longitude" in df_f.columns:
            lat_c = df_f["Latitude"].mean()
            lon_c = df_f["Longitude"].mean()
            m = folium.Map(
                location=[lat_c, lon_c], zoom_start=6,
                tiles="CartoDB dark_matter"
            )
            heat_data = df_f[["Latitude", "Longitude"]].dropna().values.tolist()
            HeatMap(
                heat_data, radius=14, blur=12, max_zoom=1,
                gradient={0.2: "#0ea5e9", 0.5: "#f59e0b", 0.8: "#e74c3c", 1.0: "#c0392b"}
            ).add_to(m)
            st_folium(m, height=400, use_container_width=True, returned_objects=[])
        else:
            st.error("Coordonnées GPS manquantes dans les données.")

    with col_chart:
        st.markdown(f"##### {T['b2_chart_quartiers']}")
        top_q = df_f["Quartier"].value_counts().head(10).reset_index()
        top_q.columns = ["Quartier", "Alertes"]
        fig = px.bar(
            top_q, x="Alertes", y="Quartier", orientation="h",
            color="Alertes", color_continuous_scale="Blues",
            text="Alertes", labels={"Alertes": "", "Quartier": ""}
        )
        fig.update_layout(
            margin=dict(l=10, r=30, t=10, b=10), height=185,
            yaxis={"categoryorder": "total ascending", "tickfont": dict(size=12)},
            xaxis={"tickfont": dict(size=11)},
            coloraxis_showscale=False,
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        fig.update_traces(textposition="outside", textfont_size=12, cliponaxis=False)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

        st.markdown(f"##### {T['b2_chart_regions']}")
        if "Region" in df_f.columns:
            reg = df_f["Region"].value_counts().reset_index()
            reg.columns = ["Région", "Alertes"]
            fig2 = px.bar(
                reg, x="Région", y="Alertes",
                color="Alertes", color_continuous_scale="Reds",
                text="Alertes", labels={"Alertes": "", "Région": ""}
            )
            fig2.update_layout(
                margin=dict(l=10, r=10, t=10, b=60), height=185,
                xaxis={"tickangle": -40, "tickfont": dict(size=10)},
                yaxis={"tickfont": dict(size=11)},
                coloraxis_showscale=False,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
            )
            fig2.update_traces(textposition="outside", textfont_size=11, cliponaxis=False)
            st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
