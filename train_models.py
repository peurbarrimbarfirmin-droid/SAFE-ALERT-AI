# SAFE-ALERT-AI — Entraînement des modèles IA
# Modèle 1 : Random Forest → Classification de l'urgence
# Modèle 2 : TF-IDF + Logistic Regression → Analyse de texte (NLP)
# Usage : python train_models.py

import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

print("=" * 60)
print("🤖 SAFE-ALERT-AI — Entraînement des modèles IA")
print("=" * 60)

# ─────────────────────────────────────────────────────────────────────────────
# 0. CHARGEMENT DES DONNÉES
# ─────────────────────────────────────────────────────────────────────────────

DATA_PATH = "data/processed/alertes_cameroun_final.csv"

if not os.path.exists(DATA_PATH):
    print(f"❌ Fichier introuvable : {DATA_PATH}")
    print("   Lance d'abord : python generate_data.py")
    exit(1)

df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
print(f"✅ Dataset chargé : {len(df)} alertes\n")

os.makedirs("models", exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# MODÈLE 1 — RANDOM FOREST : Prédiction du niveau d'urgence
# ─────────────────────────────────────────────────────────────────────────────

print("─" * 60)
print("🌲 MODÈLE 1 : Random Forest — Niveau d'urgence")
print("─" * 60)

# Features numériques + catégorielles
features_rf = [
    "Heure_num",
    "Nombre_signalements",
    "Mois",
    "Type_incident_enc",
    "Ville_enc",
    "Jour_enc",
]

# Encodage des variables catégorielles
le_type = LabelEncoder()
le_ville = LabelEncoder()
le_jour  = LabelEncoder()
le_urgence = LabelEncoder()

df["Type_incident_enc"] = le_type.fit_transform(df["Type_incident"])
df["Ville_enc"]         = le_ville.fit_transform(df["Ville"])
df["Jour_enc"]          = le_jour.fit_transform(df["Jour_semaine"])
df["Urgence_enc"]       = le_urgence.fit_transform(df["Niveau_urgence"])

# Préparation X / y
X_rf = df[features_rf]
y_rf = df["Urgence_enc"]

X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(
    X_rf, y_rf, test_size=0.20, random_state=42, stratify=y_rf
)

# Entraînement
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    min_samples_split=5,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train_rf, y_train_rf)

# Évaluation
y_pred_rf = rf_model.predict(X_test_rf)
acc_rf = accuracy_score(y_test_rf, y_pred_rf)
print(f"  ✅ Accuracy : {acc_rf*100:.1f}%")
print(f"\n  Rapport de classification :")
print(classification_report(
    y_test_rf, y_pred_rf,
    target_names=le_urgence.classes_,
    zero_division=0
))

# Importance des features
importances = pd.Series(rf_model.feature_importances_, index=features_rf)
print("  Importance des variables :")
for feat, imp in importances.sort_values(ascending=False).items():
    bar = "█" * int(imp * 40)
    print(f"    {feat:<25} {bar} {imp:.3f}")

# Sauvegarde
joblib.dump(rf_model, "models/rf_urgence.pkl")
joblib.dump(le_type,  "models/le_type_incident.pkl")
joblib.dump(le_ville, "models/le_ville.pkl")
joblib.dump(le_jour,  "models/le_jour.pkl")
joblib.dump(le_urgence, "models/le_urgence.pkl")
joblib.dump(features_rf, "models/features_rf.pkl")

print("\n  💾 Modèle sauvegardé → models/rf_urgence.pkl")

# ─────────────────────────────────────────────────────────────────────────────
# MODÈLE 2 — TF-IDF + LOGISTIC REGRESSION : Analyse de texte NLP
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "─" * 60)
print("📝 MODÈLE 2 : TF-IDF + Logistic Regression — Analyse de texte")
print("─" * 60)

# Features : description textuelle → Type d'incident
X_nlp = df["Description"]
y_nlp = df["Type_incident"]

X_train_nlp, X_test_nlp, y_train_nlp, y_test_nlp = train_test_split(
    X_nlp, y_nlp, test_size=0.20, random_state=42, stratify=y_nlp
)

# Pipeline TF-IDF + Logistic Regression
nlp_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000,
        min_df=2,
        sublinear_tf=True
    )),
    ("clf", LogisticRegression(
        max_iter=1000,
        C=5.0,
        class_weight="balanced",
        random_state=42,
        solver="lbfgs"
    ))
])

nlp_pipeline.fit(X_train_nlp, y_train_nlp)

# Évaluation
y_pred_nlp = nlp_pipeline.predict(X_test_nlp)
acc_nlp = accuracy_score(y_test_nlp, y_pred_nlp)
print(f"  ✅ Accuracy : {acc_nlp*100:.1f}%")
print(f"\n  Rapport de classification :")
print(classification_report(y_test_nlp, y_pred_nlp, zero_division=0))

# Sauvegarde
joblib.dump(nlp_pipeline, "models/nlp_pipeline.pkl")
print("  💾 Pipeline NLP sauvegardé → models/nlp_pipeline.pkl")

# ─────────────────────────────────────────────────────────────────────────────
# MODÈLE 3 — URGENCE DEPUIS TEXTE (combo NLP → urgence)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "─" * 60)
print("🚨 MODÈLE 3 : TF-IDF → Prédiction urgence depuis texte")
print("─" * 60)

X_train_urg, X_test_urg, y_train_urg, y_test_urg = train_test_split(
    X_nlp, df["Niveau_urgence"], test_size=0.20, random_state=42,
    stratify=df["Niveau_urgence"]
)

urgence_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000,
        min_df=2,
        sublinear_tf=True
    )),
    ("clf", LogisticRegression(
        max_iter=1000,
        C=3.0,
        class_weight="balanced",
        random_state=42,
        solver="lbfgs"
    ))
])

urgence_pipeline.fit(X_train_urg, y_train_urg)
y_pred_urg = urgence_pipeline.predict(X_test_urg)
acc_urg = accuracy_score(y_test_urg, y_pred_urg)
print(f"  ✅ Accuracy : {acc_urg*100:.1f}%")
print(f"\n  Rapport de classification :")
print(classification_report(y_test_urg, y_pred_urg, zero_division=0))

joblib.dump(urgence_pipeline, "models/nlp_urgence_pipeline.pkl")
print("  💾 Pipeline urgence→texte sauvegardé → models/nlp_urgence_pipeline.pkl")

# ─────────────────────────────────────────────────────────────────────────────
# RÉSUMÉ FINAL
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("🏆 RÉSUMÉ DES MODÈLES")
print("=" * 60)
print(f"  Modèle 1 — Random Forest (urgence)   : {acc_rf*100:.1f}% accuracy")
print(f"  Modèle 2 — NLP → Type incident       : {acc_nlp*100:.1f}% accuracy")
print(f"  Modèle 3 — NLP → Niveau urgence      : {acc_urg*100:.1f}% accuracy")
print("\n  Fichiers sauvegardés dans models/ :")
for f in os.listdir("models"):
    size = os.path.getsize(f"models/{f}")
    print(f"    📦 {f:<35} {size/1024:.1f} KB")

print("\n✅ Entraînement terminé ! Prêt pour le dashboard.")
print("=" * 60)
