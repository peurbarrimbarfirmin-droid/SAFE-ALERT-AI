"""
assets.py — SAFE-ALERT-AI
Définition des chemins et URLs pour les images et icônes.
"""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

IMAGES = {
    # On garde une image de fond premium, de type technologique/sécurité ou ciel dramatique
    "bg_app": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", 
    "sidebar_top": "https://images.unsplash.com/photo-1584433144859-1fc3ab64a957?q=80&w=2000&auto=format&fit=crop", # Sécurité urbaine / lumières
    "logo_fallback": "🛡️"
}
