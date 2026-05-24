# SAFE-ALERT-AI — Gestion des assets (images, logos)

import base64
import os


def get_image_base64(image_path: str) -> str:
    """Encode une image en base64 pour l'affichage Streamlit."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""


def get_logo_html(logo_path: str, width: int = 80) -> str:
    """Retourne le HTML pour afficher le logo."""
    b64 = get_image_base64(logo_path)
    if b64:
        return f'<img src="data:image/jpeg;base64,{b64}" width="{width}"/>'
    return "🛡️ SAFE-ALERT-AI"
