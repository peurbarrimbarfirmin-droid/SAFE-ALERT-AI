# SAFE-ALERT-AI — API FastAPI
# Point d'entrée principal de l'API REST

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SAFE-ALERT-AI API",
    description="Système d'aide à la décision pour la sécurité alimentaire — API REST",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "SAFE-ALERT-AI API — Bienvenue", "version": "1.0.0"}


@app.get("/zones")
def get_zones():
    """Liste toutes les zones surveillées."""
    return {"zones": []}


@app.get("/predict/{zone}")
def predict(zone: str):
    """Prédictions pour une zone donnée."""
    return {"zone": zone, "predictions": []}


@app.get("/alerte/{zone}")
def alerte(zone: str):
    """Niveau d'alerte et recommandations pour une zone."""
    return {"zone": zone, "niveau": "FAIBLE", "recommandations": []}


@app.get("/national")
def national():
    """Résumé national."""
    return {"resume": {}}


@app.get("/historique/{zone}")
def historique(zone: str):
    """Historique des données pour une zone."""
    return {"zone": zone, "historique": []}


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
