# API — SAFE-ALERT-AI

## Description

API FastAPI exposant les endpoints REST du système SAFE-ALERT-AI.

## Endpoints

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/zones` | Liste toutes les zones surveillées |
| GET | `/predict/{zone}` | Prédictions pour une zone |
| GET | `/alerte/{zone}` | Niveau d'alerte + recommandations |
| GET | `/national` | Résumé national |
| GET | `/historique/{zone}` | Historique des données |

## Lancer l'API

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Documentation interactive : `http://localhost:8000/docs`
