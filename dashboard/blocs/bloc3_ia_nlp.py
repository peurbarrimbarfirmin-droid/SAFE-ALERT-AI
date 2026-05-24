# SAFE-ALERT-AI — Onglet 3 : Intelligence Artificielle & NLP
import streamlit as st
import pandas as pd
import numpy as np
from utils import get_urgence_style, prediction_card_html, get_recommandation, score_danger, filter_dataframe_by_geo
from translations import get_t
from icons import icon


def render_bloc3_ia(df: pd.DataFrame, modeles: dict):
    T = get_t(st.session_state.get("lang", "fr"))
    lang = st.session_state.get("lang", "fr")

    # ── FILTRES ───────────────────────────────────────────────────────────────
    df_f = filter_dataframe_by_geo(df, "b3", T)

    # ── PANNEAU SAISIE / RÉSULTAT ─────────────────────────────────────────────
    col_in, col_out = st.columns([1.1, 1], gap="large")

    with col_in:
        st.markdown(f"**{T['b3_input_title']}**")
        st.markdown("<hr style='margin:0.5rem 0;'>", unsafe_allow_html=True)

        exemples = {
            "fr": [
                "Un gros accident de moto au carrefour Ndokotti, plusieurs blessés au sol.",
                "Un enfant de 7 ans disparu au marché Mokolo depuis 3 heures.",
                "Agression à main armée au rond-point Deido vers 22h.",
                "Incendie dans un immeuble à Bastos, habitants évacués.",
                "Vol de téléphone à l'arraché près du lycée de Biyem-Assi.",
            ],
            "en": [
                "A serious motorcycle accident at Ndokotti crossroads, several injured.",
                "A 7-year-old child missing at Mokolo market for 3 hours.",
                "Armed robbery at Deido roundabout around 10 PM.",
                "Fire in a building in Bastos, residents evacuated.",
                "Phone snatching near Biyem-Assi high school.",
            ]
        }
        lang = st.session_state.get("lang", "fr")
        ex = exemples.get(lang, exemples["fr"])

        exemple_sel = st.selectbox(
            "💡 Exemple rapide :" if lang == "fr" else "💡 Quick example:",
            [""] + ex, key="ex_ia"
        )
        texte_defaut = exemple_sel if exemple_sel else ex[0]

        texte = st.text_area(
            label=T["b3_input_title"],
            value=texte_defaut,
            height=130,
            label_visibility="collapsed",
            key="txt_ia"
        )

        analyser = st.button(T["b3_btn"], type="primary", use_container_width=True)

        # Statistiques de la zone filtrée
        if not df_f.empty:
            st.markdown("<hr style='opacity:0.15; margin:0.8rem 0;'>", unsafe_allow_html=True)
            st.markdown("**📊 Contexte zone sélectionnée :**" if lang == "fr" else "**📊 Selected zone context:**")
            n_tot = len(df_f)
            n_crit = len(df_f[df_f["Niveau_urgence"] == "CRITIQUE"])
            pct = n_crit / n_tot * 100 if n_tot > 0 else 0
            top_t = df_f["Type_incident"].value_counts().index[0] if n_tot > 0 else "N/A"
            st.markdown(f"- **{n_tot:,}** alertes analysées  \n- **{n_crit}** critiques ({pct:.1f}%)  \n- Type dominant : **{top_t}**")

    with col_out:
        st.markdown(f"#### {T['b3_result_title']}")

        if analyser and texte.strip():
            has_nlp_type    = "nlp_type"    in modeles
            has_nlp_urgence = "nlp_urgence" in modeles

            if has_nlp_type and has_nlp_urgence:
                with st.spinner("🧠 Analyse NLP en cours..." if lang == "fr" else "🧠 Running NLP analysis..."):
                    # Prédiction type
                    type_pred  = modeles["nlp_type"].predict([texte])[0]
                    type_proba = float(np.max(modeles["nlp_type"].predict_proba([texte]))) * 100

                    # Prédiction urgence
                    urg_pred   = modeles["nlp_urgence"].predict([texte])[0]
                    urg_proba  = float(np.max(modeles["nlp_urgence"].predict_proba([texte]))) * 100

                    # Indicateurs dérivés
                    s = score_danger(urg_pred)
                    reco = get_recommandation(urg_pred)

                    ressources = "🚓 Police"
                    txt_low = texte.lower()
                    if any(w in txt_low for w in ["blessé", "accident", "urgence", "injured", "accident"]):
                        ressources += " + 🚑 SAMU"
                    if urg_pred == "CRITIQUE":
                        ressources += " + 🚒 Sapeurs-Pompiers" if lang == "fr" else " + 🚒 Firefighters"
                    if "incendie" in txt_low or "fire" in txt_low:
                        ressources = "🚒 Sapeurs-Pompiers + 🚓 Police" if lang == "fr" else "🚒 Firefighters + 🚓 Police"
                    if "enfant" in txt_low or "child" in txt_low or "disparu" in txt_low or "missing" in txt_low:
                        ressources = "🚓 Police + 👨‍👩‍👧 Protection de l'Enfance" if lang == "fr" else "🚓 Police + 👨‍👩‍👧 Child Protection"

                    temps_map = {"CRITIQUE": "5-10 min", "ÉLEVÉ": "15-20 min", "MOYEN": "30-45 min", "FAIBLE": "1-2h"}
                    temps = temps_map.get(urg_pred, "N/A")

                    st.markdown(
                        prediction_card_html(type_pred, urg_pred, s, reco, type_proba, urg_proba, ressources, temps),
                        unsafe_allow_html=True
                    )
            else:
                st.error("❌ Modèles IA non chargés. Exécutez `train_models.py` d'abord.")
        elif not analyser:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.04); border:1.5px dashed rgba(128,128,128,0.35);
                        border-radius:14px; padding:2rem; text-align:center; margin-top:0.5rem;">
                <div style="font-size:2.5rem; margin-bottom:0.5rem;">🤖</div>
                <div style="font-size:1.1rem; font-weight:700; color:#aaa; margin-bottom:0.3rem;">{T['b3_waiting']}</div>
                <div style="font-size:0.85rem; color:#666;">{T['b3_waiting_sub']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Veuillez saisir un texte avant d'analyser." if lang == "fr" else "⚠️ Please enter a text before analyzing.")
