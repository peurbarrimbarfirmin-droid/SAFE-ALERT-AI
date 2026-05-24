FROM python:3.11-slim

# Répertoire de travail
WORKDIR /app

# Dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie du code
COPY . .

# Port (Hugging Face Spaces : 7860 | Render : variable $PORT)
ENV PORT=7860
EXPOSE 7860

# Lancement de l'API
CMD ["python", "api/main.py"]
