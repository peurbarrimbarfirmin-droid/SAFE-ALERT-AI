# SAFE-ALERT-AI — Onglet 1 : Vue Générale & KPIs Nationaux
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import kpi_card_html, get_urgence_style, filter_dataframe_by_geo
from translations import get_t
from icons import icon


def render_bloc1_vue_generale(df: pd.DataFrame):
    T = get_t(st.session_state.get("lang", "fr"))

    # ── FILTRES VILLE / QUARTIER ──────────────────────────────────────────────
    df_f = filter_dataframe_by_geo(df, "b1", T)
    if df_f.empty:
        st.warning("⚠️ Aucune donnée pour cette sélection.")
        return

    # ── KPI CARDS ─────────────────────────────────────────────────────────────
    total       = len(df_f)
    critiques   = len(df_f[df_f["Niveau_urgence"] == "CRITIQUE"])
    resolues    = len(df_f[df_f.get("Statut", pd.Series(dtype=str)) == "Résolu"]) if "Statut" in df_f.columns else 0
    temps_moy   = df_f["Temps_intervention_minutes"].mean() if "Temps_intervention_minutes" in df_f.columns else 45
    top_zone    = df_f["Quartier"].value_counts().index[0] if total > 0 else "N/A"

    pct_crit  = critiques / total * 100 if total > 0 else 0
    pct_resol = resolues / total * 100 if total > 0 else 0

    k1, k2, k3, k4, k5 = st.columns(5)
    k1.markdown(kpi_card_html(T["kpi_total"],    f"{total:,}".replace(",", " "),  T["kpi_sub_total"],   "#e74c3c", "📡"), unsafe_allow_html=True)
    k2.markdown(kpi_card_html(T["kpi_critique"], f"{critiques:,}".replace(",", " "), f"{pct_crit:.1f}% {T['kpi_sub_critique']}", "#c0392b", "🚨"), unsafe_allow_html=True)
    k3.markdown(kpi_card_html(T["kpi_resolues"], f"{resolues:,}".replace(",", " "),  f"{pct_resol:.1f}% {T['kpi_sub_resolues']}", "#27ae60", "✅"), unsafe_allow_html=True)
    k4.markdown(kpi_card_html(T["kpi_temps"],    f"{int(temps_moy)} min",           T["kpi_sub_temps"],   "#0ea5e9", "⏱️"), unsafe_allow_html=True)
    k5.markdown(kpi_card_html(T["kpi_zone"],     top_zone,                          T["kpi_sub_zone"],    "#8e44ad", "📍"), unsafe_allow_html=True)

    st.markdown("<hr style='opacity:0.15; margin:1rem 0;'>", unsafe_allow_html=True)

    # ── ROW 1 : Évolution temporelle + Répartition Urgences ───────────────────
    col_l, col_r = st.columns([1.6, 1], gap="large")

    with col_l:
        st.markdown(f"##### {T['chart_evol']}")
        df_f["Mois"] = df_f["Date"].dt.to_period("M").astype(str)
        evol = df_f.groupby(["Mois", "Niveau_urgence"]).size().reset_index(name="N")
        ordre_urg = ["CRITIQUE", "ÉLEVÉ", "MOYEN", "FAIBLE"]
        color_map = {u: get_urgence_style(u)["color"] for u in ordre_urg}
        fig = px.bar(
            evol, x="Mois", y="N", color="Niveau_urgence",
            color_discrete_map=color_map,
            category_orders={"Niveau_urgence": ordre_urg},
            labels={"N": "", "Mois": "", "Niveau_urgence": ""},
            barmode="stack"
        )
        fig.update_layout(
            margin=dict(l=10, r=10, t=10, b=60), height=280,
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=False, tickangle=-45, tickfont=dict(size=11)),
            yaxis=dict(showgrid=True, gridcolor="rgba(128,128,128,0.2)", tickfont=dict(size=12)),
            legend=dict(orientation="h", yanchor="bottom", y=-0.55, xanchor="center", x=0.5, font=dict(size=11))
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    with col_r:
        st.markdown(f"##### {T['chart_types']}")
        types = df_f["Type_incident"].value_counts().reset_index()
        types.columns = ["Type", "Count"]
        fig2 = px.pie(
            types, names="Type", values="Count", hole=0.55,
            color_discrete_sequence=["#e74c3c","#e67e22","#f39c12","#8e44ad","#0ea5e9","#27ae60","#2c3e50"]
        )
        fig2.update_layout(
            margin=dict(l=0, r=0, t=10, b=10), height=280,
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=-0.35, xanchor="center", x=0.5, font=dict(size=10))
        )
        fig2.update_traces(textinfo="percent", textfont_size=12)
        st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

    # ── ROW 2 : Top Villes + Top Quartiers ────────────────────────────────────
    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown(f"##### {T['chart_villes']}")
        villes = df_f["Ville"].value_counts().head(10).reset_index()
        villes.columns = ["Ville", "Alertes"]
        fig3 = px.bar(
            villes, x="Alertes", y="Ville", orientation="h",
            color="Alertes", color_continuous_scale="Reds",
            text="Alertes", labels={"Alertes": "", "Ville": ""}
        )
        fig3.update_layout(
            margin=dict(l=10, r=30, t=10, b=10), height=260,
            yaxis={"categoryorder": "total ascending", "tickfont": dict(size=12)},
            xaxis={"tickfont": dict(size=11)},
            coloraxis_showscale=False,
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        fig3.update_traces(textposition="outside", textfont_size=12, cliponaxis=False)
        st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

    with col_b:
        st.markdown(f"##### {T['chart_top_quartiers']}")
        qts = df_f["Quartier"].value_counts().head(10).reset_index()
        qts.columns = ["Quartier", "Alertes"]
        fig4 = px.bar(
            qts, x="Alertes", y="Quartier", orientation="h",
            color="Alertes", color_continuous_scale="Oranges",
            text="Alertes", labels={"Alertes": "", "Quartier": ""}
        )
        fig4.update_layout(
            margin=dict(l=10, r=30, t=10, b=10), height=260,
            yaxis={"categoryorder": "total ascending", "tickfont": dict(size=12)},
            xaxis={"tickfont": dict(size=11)},
            coloraxis_showscale=False,
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        fig4.update_traces(textposition="outside", textfont_size=12, cliponaxis=False)
        st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})
