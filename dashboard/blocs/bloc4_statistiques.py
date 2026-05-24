# SAFE-ALERT-AI — Onglet 4 : Statistiques & Tendances
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import kpi_card_html, filter_dataframe_by_geo
from translations import get_t

JOURS_FR = {"Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi",
            "Thursday": "Jeudi", "Friday": "Vendredi", "Saturday": "Samedi", "Sunday": "Dimanche"}
JOURS_EN = {v: k for k, v in JOURS_FR.items()}
JOURS_ORDER_FR = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
JOURS_ORDER_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def render_bloc4_statistiques(df: pd.DataFrame):
    T   = get_t(st.session_state.get("lang", "fr"))
    lang = st.session_state.get("lang", "fr")

    # ── FILTRES ───────────────────────────────────────────────────────────────
    df_f = filter_dataframe_by_geo(df, "b4", T)
    if df_f.empty:
        st.warning("⚠️ Aucune donnée pour cette sélection.")
        return

    # ── KPIs STATISTIQUES ─────────────────────────────────────────────────────
    if "Heure" in df_f.columns:
        heure_pic = df_f["Heure"].value_counts().index[0]
    else:
        heure_pic = "N/A"
    top_cat  = df_f["Type_incident"].value_counts().index[0] if len(df_f) > 0 else "N/A"

    # Tendance : comparer première et dernière semaine
    df_f_sorted = df_f.sort_values("Date")
    mid = len(df_f_sorted) // 2
    trend_1h = len(df_f_sorted.iloc[:mid])
    trend_2h = len(df_f_sorted.iloc[mid:])
    if trend_2h > trend_1h:
        trend_txt = "📈 En hausse" if lang == "fr" else "📈 Increasing"
        trend_col = "#e74c3c"
    else:
        trend_txt = "📉 En baisse" if lang == "fr" else "📉 Decreasing"
        trend_col = "#27ae60"

    k1, k2, k3 = st.columns(3)
    k1.markdown(kpi_card_html(T["b4_kpi_heure"], f"{heure_pic}h00",  "Pic de dangerosité" if lang == "fr" else "Peak danger time",   "#f59e0b", "🕒"), unsafe_allow_html=True)
    k2.markdown(kpi_card_html(T["b4_kpi_cat"],   top_cat,            "Incident le plus fréquent" if lang == "fr" else "Most frequent", "#e74c3c", "🏷️"), unsafe_allow_html=True)
    k3.markdown(kpi_card_html(T["b4_kpi_trend"], trend_txt,          "Sur la période sélectionnée" if lang == "fr" else "Over selected period", trend_col, "📊"), unsafe_allow_html=True)

    st.markdown("<hr style='opacity:0.15; margin:1rem 0;'>", unsafe_allow_html=True)

    # ── ROW 1 : Incidents par heure + par jour ────────────────────────────────
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f"##### {T['b4_heure']}")
        if "Heure" in df_f.columns:
            h_data = df_f.groupby(["Heure", "Niveau_urgence"]).size().reset_index(name="N")
            fig1 = px.bar(
                h_data, x="Heure", y="N", color="Niveau_urgence",
                color_discrete_map={"CRITIQUE": "#e74c3c", "ÉLEVÉ": "#e67e22", "MOYEN": "#f39c12", "FAIBLE": "#27ae60"},
                labels={"N": "", "Heure": "", "Niveau_urgence": ""}
            )
            fig1.update_layout(
                margin=dict(l=10, r=10, t=10, b=40), height=260,
                xaxis=dict(tickmode="linear", tick0=0, dtick=2, tickfont=dict(size=12)),
                yaxis=dict(tickfont=dict(size=12), gridcolor="rgba(128,128,128,0.15)"),
                barmode="stack",
                legend=dict(orientation="h", y=-0.35, xanchor="center", x=0.5, font=dict(size=10)),
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig1, use_container_width=True, config={"displayModeBar": False})

    with col2:
        st.markdown(f"##### {T['b4_jour']}")
        if "Jour_semaine" in df_f.columns:
            if lang == "fr":
                df_tmp = df_f.copy()
                df_tmp["Jour_FR"] = df_tmp["Jour_semaine"].map(JOURS_FR)
                j_data = df_tmp.groupby("Jour_FR").size().reindex(JOURS_ORDER_FR).reset_index(name="N")
                j_data.columns = ["Jour", "N"]
            else:
                j_data = df_f.groupby("Jour_semaine").size().reindex(JOURS_ORDER_EN).reset_index(name="N")
                j_data.columns = ["Jour", "N"]

            fig2 = px.bar(
                j_data, x="Jour", y="N",
                color="N", color_continuous_scale="Reds",
                text="N", labels={"N": "", "Jour": ""}
            )
            fig2.update_layout(
                margin=dict(l=10, r=10, t=10, b=60), height=260,
                xaxis=dict(tickangle=-45, tickfont=dict(size=12)),
                yaxis=dict(tickfont=dict(size=12), gridcolor="rgba(128,128,128,0.15)"),
                coloraxis_showscale=False,
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
            )
            fig2.update_traces(textposition="outside", textfont_size=12, cliponaxis=False)
            st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

    # ── ROW 2 : Évolution mensuelle + Fréquence par type ─────────────────────
    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown(f"##### {T['b4_mois']}")
        df_f["Mois"] = df_f["Date"].dt.to_period("M").astype(str)
        mois_data = df_f.groupby("Mois").size().reset_index(name="N")
        fig3 = px.area(
            mois_data, x="Mois", y="N",
            color_discrete_sequence=["#f59e0b"],
            labels={"N": "", "Mois": ""}
        )
        fig3.update_layout(
            margin=dict(l=10, r=10, t=10, b=60), height=240,
            xaxis=dict(tickangle=-45, tickfont=dict(size=10), showgrid=False),
            yaxis=dict(tickfont=dict(size=12), gridcolor="rgba(128,128,128,0.15)"),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        fig3.update_traces(fill="tozeroy", fillcolor="rgba(245,158,11,0.2)")
        st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

    with col4:
        st.markdown(f"##### {T['b4_freq']}")
        type_data = df_f["Type_incident"].value_counts().reset_index()
        type_data.columns = ["Type", "N"]
        fig4 = px.bar(
            type_data, x="N", y="Type", orientation="h",
            color="N", color_continuous_scale="Purples",
            text="N", labels={"N": "", "Type": ""}
        )
        fig4.update_layout(
            margin=dict(l=10, r=30, t=10, b=10), height=240,
            yaxis={"categoryorder": "total ascending", "tickfont": dict(size=12)},
            xaxis={"tickfont": dict(size=11)},
            coloraxis_showscale=False,
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        fig4.update_traces(textposition="outside", textfont_size=12, cliponaxis=False)
        st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})
