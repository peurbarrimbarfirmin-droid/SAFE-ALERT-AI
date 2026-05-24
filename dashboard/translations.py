"""
translations.py — SAFE-ALERT-AI
Dictionnaire bilingue pour l'interface de l'application.
"""

TRANSLATIONS = {
    "fr": {
        "sidebar_app_subtitle": "POUR UNE COMMUNAUTÉ PLUS SÛRE",
        "sidebar_theme_title": "THÈME",
        "sidebar_lang_title": "LANGUE",
        "sidebar_theme_dark": "Sombre",
        "sidebar_theme_light": "Clair",
        "sidebar_period_label": "Période (Années)",
        "sidebar_date_start": "Date début",
        "sidebar_date_end": "Date fin",
        "sidebar_footer": "© 2026 SAFE-ALERT-AI\nHackathon IndabaX Cameroon",
        
        "tab_generale": "🏠 Vue Générale",
        "tab_geo": "📍 Analyse Géo",
        "tab_ia": "🧠 IA & Prédiction",
        "tab_stats": "📈 Statistiques",
        "tab_gestion": "📋 Alertes",

        # Filtres
        "filter_city": "🏙️ Ville",
        "filter_neighborhood": "📍 Quartier",
        "filter_status": "Statut",
        "filter_priority": "Priorité (Urgence)",
        "filter_type": "🏷️ Type d'incident",
        "filter_all": "Tous",
        "filter_all_f": "Toutes",
        
        # Bloc 1
        "b1_title": "🏠 Vue Générale — Tableau de bord national",
        "kpi_total": "Total alertes",
        "kpi_critique": "Alertes critiques",
        "kpi_resolues": "Alertes résolues",
        "kpi_temps": "Temps d'intervention",
        "kpi_zone": "Zone à risque",
        "kpi_sub_total": "Jan 2024 – Mai 2025",
        "kpi_sub_critique": "du total",
        "kpi_sub_resolues": "de résolution",
        "kpi_sub_temps": "Toutes urgences confondues",
        "kpi_sub_zone": "Indice : ÉLEVÉ",
        "chart_evol": "📈 Évolution des alertes dans le temps",
        "chart_types": "🍩 Types d'incidents",
        "chart_villes": "🏙️ Alertes par ville",
        "chart_top_quartiers": "📍 Top 10 quartiers à risque",
        
        # Bloc 2
        "b2_title": "📍 Analyse Géographique — Cartographie des risques",
        "b2_map_title": "🗺️ Carte des alertes — Heatmap des zones dangereuses",
        "b2_kpi_title": "📊 Indicateurs clés",
        "b2_kpi_quartier": "Quartier le plus touché",
        "b2_kpi_zones": "Zones surveillées",
        "b2_kpi_temps": "Temps intervention moyen",
        "b2_chart_quartiers": "🏙️ Alertes par quartier (Top 10)",
        "b2_chart_regions": "🗺️ Niveau de risque par région",

        # Bloc 3 (IA)
        "b3_title": "🧠 Intelligence Artificielle — Analyse automatique",
        "b3_desc": "Saisissez la description d'un incident tel qu'il pourrait être signalé par un citoyen. L'IA extraira la catégorie et déterminera le niveau d'urgence.",
        "b3_input_title": "📝 Entrez la description de l'incident",
        "b3_btn": "🚀 Analyser l'alerte",
        "b3_result_title": "⚙️ Résultat de l'IA",
        "b3_waiting": "🤖 En attente",
        "b3_waiting_sub": "Cliquez sur 'Analyser l'alerte' pour voir le résultat.",
        
        # Bloc 4 (Statistiques)
        "b4_title": "📈 Analyse Statistique — Tendances et saisonnalité",
        "b4_heure": "🕒 Incidents selon l'heure",
        "b4_jour": "📅 Incidents selon le jour",
        "b4_mois": "📊 Évolution mensuelle",
        "b4_freq": "📋 Types d'incidents fréquents",
        "b4_kpis": "💡 Indicateurs clés d'analyse",
        "b4_kpi_heure": "Heure la plus dangereuse",
        "b4_kpi_cat": "Catégorie dominante",
        "b4_kpi_trend": "Tendance temporelle",
        
        # Bloc 5 (Gestion)
        "b5_title": "📋 Gestion des alertes — Table des signalements",
        "b5_search": "🔍 Recherche (ID, type, description...)",
        "b5_total": "Total : {count} alertes correspondantes",
        "b5_details": "🔎 Détails d'une alerte",
        "b5_details_desc": "Sélectionnez un ID d'alerte pour voir la description complète :",
        "b5_none": "Aucun"
    },
    "en": {
        "sidebar_app_subtitle": "FOR A SAFER COMMUNITY",
        "sidebar_theme_title": "THEME",
        "sidebar_lang_title": "LANGUAGE",
        "sidebar_theme_dark": "Dark",
        "sidebar_theme_light": "Light",
        "sidebar_period_label": "Period (Years)",
        "sidebar_date_start": "Start Date",
        "sidebar_date_end": "End Date",
        "sidebar_footer": "© 2026 SAFE-ALERT-AI\nHackathon IndabaX Cameroon",
        
        "tab_generale": "🏠 Overview",
        "tab_geo": "📍 Geo Analysis",
        "tab_ia": "🧠 AI Prediction",
        "tab_stats": "📈 Statistics",
        "tab_gestion": "📋 Alerts Mgt",

        # Filters
        "filter_city": "🏙️ City",
        "filter_neighborhood": "📍 Neighborhood",
        "filter_status": "Status",
        "filter_priority": "Priority (Urgency)",
        "filter_type": "🏷️ Incident Type",
        "filter_all": "All",
        "filter_all_f": "All",
        
        # Block 1
        "b1_title": "🏠 Overview — National Dashboard",
        "kpi_total": "Total alerts",
        "kpi_critique": "Critical alerts",
        "kpi_resolues": "Resolved alerts",
        "kpi_temps": "Response time",
        "kpi_zone": "High risk zone",
        "kpi_sub_total": "Jan 2024 – May 2025",
        "kpi_sub_critique": "of total",
        "kpi_sub_resolues": "resolution rate",
        "kpi_sub_temps": "All emergencies combined",
        "kpi_sub_zone": "Index: HIGH",
        "chart_evol": "📈 Alert evolution over time",
        "chart_types": "🍩 Incident types",
        "chart_villes": "🏙️ Alerts by city",
        "chart_top_quartiers": "📍 Top 10 high-risk neighborhoods",
        
        # Block 2
        "b2_title": "📍 Geographic Analysis — Risk Mapping",
        "b2_map_title": "🗺️ Alerts Map — Danger Zones Heatmap",
        "b2_kpi_title": "📊 Key Indicators",
        "b2_kpi_quartier": "Most affected neighborhood",
        "b2_kpi_zones": "Monitored zones",
        "b2_kpi_temps": "Average response time",
        "b2_chart_quartiers": "🏙️ Alerts by neighborhood (Top 10)",
        "b2_chart_regions": "🗺️ Risk level by region",

        # Block 3 (IA)
        "b3_title": "🧠 Artificial Intelligence — Automated Analysis",
        "b3_desc": "Enter the description of an incident as it might be reported by a citizen. The AI will extract the category and determine the urgency level.",
        "b3_input_title": "📝 Enter incident description",
        "b3_btn": "🚀 Analyze Alert",
        "b3_result_title": "⚙️ AI Result",
        "b3_waiting": "🤖 Waiting",
        "b3_waiting_sub": "Click on 'Analyze Alert' to see the result.",
        
        # Block 4 (Statistics)
        "b4_title": "📈 Statistical Analysis — Trends & Seasonality",
        "b4_heure": "🕒 Incidents by hour",
        "b4_jour": "📅 Incidents by day",
        "b4_mois": "📊 Monthly evolution",
        "b4_freq": "📋 Frequent incident types",
        "b4_kpis": "💡 Key Analysis Indicators",
        "b4_kpi_heure": "Most dangerous hour",
        "b4_kpi_cat": "Dominant category",
        "b4_kpi_trend": "Time trend",
        
        # Block 5 (Management)
        "b5_title": "📋 Alerts Management — Reports Table",
        "b5_search": "🔍 Search (ID, type, description...)",
        "b5_total": "Total : {count} matching alerts",
        "b5_details": "🔎 Alert Details",
        "b5_details_desc": "Select an alert ID to view the full description:",
        "b5_none": "None"
    }
}

def get_t(lang: str = "fr") -> dict:
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"])
