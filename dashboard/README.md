# Dashboard — SAFE-ALERT-AI

## Description

Interface Streamlit du système SAFE-ALERT-AI.

## Structure

```
dashboard/
├── app.py              # Point d'entrée principal
├── utils.py            # Fonctions utilitaires
├── assets.py           # Images et ressources
├── themes.py           # Thèmes et styles CSS
├── translations.py     # Traductions FR/EN
├── landing.py          # Page d'accueil / Landing page
├── chatbox.py          # Module chatbot IA
├── about/              # Page "À propos"
│   └── apropos.html
├── blocs/              # Blocs thématiques du dashboard
│   ├── bloc1_carte.py          # Carte interactive
│   ├── bloc2_kpis.py           # KPIs nationaux
│   ├── bloc3_predictions.py    # Prédictions
│   ├── bloc4_alertes.py        # Système d'alertes
│   ├── bloc5_decision.py       # Aide à la décision
│   └── bloc6_profil.py         # Profil contextuel
└── utils/              # Utilitaires internes
```

## Lancer le Dashboard

```bash
cd dashboard
streamlit run app.py
```

Le dashboard sera disponible sur `http://localhost:8501`
