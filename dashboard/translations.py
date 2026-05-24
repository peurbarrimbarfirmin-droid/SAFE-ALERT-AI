# SAFE-ALERT-AI — Traductions FR/EN

TRANSLATIONS = {
    "fr": {
        "app_title": "SAFE-ALERT-AI",
        "app_subtitle": "Système d'alerte précoce et d'aide à la décision",
        "carte": "Carte interactive",
        "kpis": "Indicateurs clés",
        "predictions": "Prédictions",
        "alertes": "Alertes",
        "decision": "Aide à la décision",
        "profil": "Profil contextuel",
        "faible": "FAIBLE",
        "modere": "MODÉRÉ",
        "eleve": "ÉLEVÉ",
        "critique": "CRITIQUE",
        "langue": "Langue",
        "a_propos": "À propos",
        "telecharger": "Télécharger le rapport",
    },
    "en": {
        "app_title": "SAFE-ALERT-AI",
        "app_subtitle": "Early Warning and Decision Support System",
        "carte": "Interactive Map",
        "kpis": "Key Indicators",
        "predictions": "Predictions",
        "alertes": "Alerts",
        "decision": "Decision Support",
        "profil": "Contextual Profile",
        "faible": "LOW",
        "modere": "MODERATE",
        "eleve": "HIGH",
        "critique": "CRITICAL",
        "langue": "Language",
        "a_propos": "About",
        "telecharger": "Download Report",
    }
}


def t(key: str, lang: str = "fr") -> str:
    """Retourne la traduction d'une clé dans la langue donnée."""
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
