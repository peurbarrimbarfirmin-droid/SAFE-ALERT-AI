# SAFE-ALERT-AI — Générateur de données simulées réalistes
# Cameroun : 10 régions, villes & quartiers réels, coordonnées GPS précises
# Usage : python generate_data.py

import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# 1. GÉOGRAPHIE DU CAMEROUN — Données réelles
# ─────────────────────────────────────────────────────────────────────────────

GEOGRAPHIE = {
    "Douala": {
        "region": "Littoral",
        "lat_base": 4.0511, "lon_base": 9.7679,
        "quartiers": {
            "Mokolo":       (4.0642, 9.7385),
            "Akwa":         (4.0500, 9.7050),
            "Bonanjo":      (4.0400, 9.6980),
            "Bonapriso":    (4.0300, 9.6900),
            "Bassa":        (4.0200, 9.7600),
            "Deido":        (4.0700, 9.7200),
            "Ndokotti":     (4.0600, 9.7500),
            "Makepe":       (4.0900, 9.7800),
            "Logbaba":      (4.0150, 9.7750),
            "New Bell":     (4.0550, 9.7300),
        },
        "poids": 0.30
    },
    "Yaoundé": {
        "region": "Centre",
        "lat_base": 3.8480, "lon_base": 11.5021,
        "quartiers": {
            "Bastos":       (3.8800, 11.5150),
            "Mvog-Mbi":     (3.8400, 11.5200),
            "Essos":        (3.8600, 11.5300),
            "Biyem-Assi":   (3.8200, 11.4900),
            "Mfoundi":      (3.8480, 11.5021),
            "Nsam":         (3.8100, 11.5100),
            "Obili":        (3.8350, 11.4800),
            "Ekounou":      (3.8000, 11.5400),
            "Nkol-Eton":    (3.8700, 11.5250),
            "Mendong":      (3.8050, 11.4750),
        },
        "poids": 0.25
    },
    "Bafoussam": {
        "region": "Ouest",
        "lat_base": 5.4737, "lon_base": 10.4175,
        "quartiers": {
            "Kamkop":       (5.4800, 10.4200),
            "Djeleng":      (5.4700, 10.4100),
            "Tamdja":       (5.4650, 10.4250),
            "Banengo":      (5.4900, 10.4050),
            "Tougang":      (5.4750, 10.4300),
        },
        "poids": 0.08
    },
    "Bamenda": {
        "region": "Nord-Ouest",
        "lat_base": 5.9527, "lon_base": 10.1463,
        "quartiers": {
            "Commercial Avenue": (5.9600, 10.1500),
            "Mile 2":           (5.9450, 10.1400),
            "Old Town":         (5.9500, 10.1350),
            "Nkwen":            (5.9700, 10.1600),
            "Cow Street":       (5.9520, 10.1480),
        },
        "poids": 0.07
    },
    "Maroua": {
        "region": "Extrême-Nord",
        "lat_base": 10.5957, "lon_base": 14.3240,
        "quartiers": {
            "Domayo":      (10.6000, 14.3300),
            "Kakataré":    (10.5900, 14.3200),
            "Hardé":       (10.5850, 14.3150),
            "Dougoi":      (10.6050, 14.3100),
            "Kodek":       (10.5950, 14.3400),
        },
        "poids": 0.08
    },
    "Garoua": {
        "region": "Nord",
        "lat_base": 9.3017, "lon_base": 13.3973,
        "quartiers": {
            "Yelwa":       (9.3100, 13.4000),
            "Marouaré":    (9.2950, 13.3900),
            "Bocklé":      (9.3050, 13.4100),
            "Plateau":     (9.3150, 13.3950),
            "Roumdé":      (9.2900, 13.4050),
        },
        "poids": 0.06
    },
    "Ngaoundéré": {
        "region": "Adamaoua",
        "lat_base": 7.3167, "lon_base": 13.5833,
        "quartiers": {
            "Dang":        (7.3200, 13.5900),
            "Mbideng":     (7.3100, 13.5750),
            "Bamyanga":    (7.3250, 13.5800),
            "Haoussa":     (7.3150, 13.5950),
            "Joli-Soir":   (7.3050, 13.5700),
        },
        "poids": 0.05
    },
    "Bertoua": {
        "region": "Est",
        "lat_base": 4.5769, "lon_base": 13.6836,
        "quartiers": {
            "Camp Sic":    (4.5800, 13.6900),
            "Nkolbikon":   (4.5700, 13.6800),
            "Haoussa":     (4.5850, 13.6750),
            "Mokolo 2":    (4.5650, 13.6950),
            "Centre-Ville": (4.5769, 13.6836),
        },
        "poids": 0.04
    },
    "Ebolowa": {
        "region": "Sud",
        "lat_base": 2.9000, "lon_base": 11.1500,
        "quartiers": {
            "Nkol-Meyos":  (2.9050, 11.1550),
            "Angalé":      (2.8950, 11.1450),
            "Centre":      (2.9000, 11.1500),
            "Mvomeka'a":   (2.9100, 11.1600),
            "Anguélé":     (2.8900, 11.1400),
        },
        "poids": 0.03
    },
    "Buea": {
        "region": "Sud-Ouest",
        "lat_base": 4.1527, "lon_base": 9.2416,
        "quartiers": {
            "Molyko":      (4.1600, 9.2500),
            "Mile 17":     (4.1450, 9.2350),
            "Bonduma":     (4.1550, 9.2450),
            "Great Soppo": (4.1700, 9.2550),
            "Clerks Quarter": (4.1500, 9.2400),
        },
        "poids": 0.04
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# 2. TYPES D'INCIDENTS & DESCRIPTIONS RÉALISTES
# ─────────────────────────────────────────────────────────────────────────────

INCIDENTS = {
    "Disparition d'enfant": {
        "poids": 0.30,
        "urgence_base": "ÉLEVÉ",
        "descriptions": [
            "Un enfant de {age} ans a disparu au marché {lieu} depuis {duree}. Portait {vetement}.",
            "Enfant disparu, {age} ans, vu pour la dernière fois près de {lieu} vers {heure}h.",
            "Parents signalent la disparition de leur enfant ({age} ans) depuis {duree} dans le quartier {lieu}.",
            "Une fillette de {age} ans introuvable depuis {duree} après l'école au niveau de {lieu}.",
            "Disparition d'un enfant de {age} ans au marché {lieu}. Signalé par {temoin} témoins.",
            "Enfant ({age} ans) manquant depuis ce matin à {lieu}. Famille très inquiète.",
            "Un garçon de {age} ans n'est pas rentré de l'école. Vu pour la dernière fois à {lieu}.",
        ]
    },
    "Agression": {
        "poids": 0.22,
        "urgence_base": "CRITIQUE",
        "descriptions": [
            "Agression à main armée signalée à {lieu} vers {heure}h. {temoin} témoins présents.",
            "Un individu a été agressé au couteau près de {lieu}. Blessé transporté à l'hôpital.",
            "Braquage en pleine rue à {lieu}. Les agresseurs ont pris {objet} et ont fui.",
            "Agression physique violente signalée au quartier {lieu}. Victime en mauvais état.",
            "Un commerçant agressé et blessé à {lieu}. Intervention urgente requise.",
            "Attaque signalée à {lieu} vers {heure}h du soir. Agresseurs en fuite.",
        ]
    },
    "Accident": {
        "poids": 0.18,
        "urgence_base": "MOYEN",
        "descriptions": [
            "Accident de moto à {lieu}, {temoin} blessés. Ambulance demandée.",
            "Collision entre un véhicule et une moto à {lieu}. Route partiellement bloquée.",
            "Accident grave de la circulation à {lieu}. Blessés signalés sur place.",
            "Renversement de passagers à {lieu}. {temoin} personnes blessées dont un enfant.",
            "Accident de moto-taxi au carrefour de {lieu}. Conducteur inconscient.",
            "Collision frontale à {lieu}. Les secours sont demandés d'urgence.",
        ]
    },
    "Vol": {
        "poids": 0.12,
        "urgence_base": "MOYEN",
        "descriptions": [
            "Vol à l'arraché signalé à {lieu}. Le malfrat a pris {objet} et a pris la fuite.",
            "Cambriolage dans une boutique à {lieu}. Dommages importants.",
            "Vol de {objet} constaté à {lieu}. Propriétaire demande assistance.",
            "Pickpocket actif au marché {lieu}. Plusieurs victimes signalées.",
            "Vol avec violence à {lieu}. Victime légèrement blessée.",
        ]
    },
    "Incendie": {
        "poids": 0.08,
        "urgence_base": "CRITIQUE",
        "descriptions": [
            "Incendie déclaré dans une maison à {lieu}. Habitants évacués. Pompiers demandés.",
            "Début d'incendie dans un marché à {lieu}. Nombreux commerçants en danger.",
            "Feu de brousse s'approchant des habitations à {lieu}. Évacuation en cours.",
            "Incendie d'un véhicule à {lieu}. Risque de propagation aux bâtiments proches.",
            "Case en feu à {lieu}. Une famille bloquée à l'intérieur. Urgence absolue.",
        ]
    },
    "Urgence médicale": {
        "poids": 0.10,
        "urgence_base": "ÉLEVÉ",
        "descriptions": [
            "Personne inconsciente à {lieu}. Ambulance demandée d'urgence.",
            "Crise cardiaque signalée à {lieu}. Le patient est dans un état critique.",
            "Femme enceinte en travail à {lieu}. Besoin d'une assistance médicale immédiate.",
            "Enfant en convulsions à {lieu}. Parents paniqués, secours demandés.",
            "Intoxication alimentaire collective à {lieu}. Plusieurs personnes touchées.",
            "Noyade au fleuve près de {lieu}. Intervention urgente des secours.",
        ]
    },
}

OBJETS = ["un téléphone", "un sac à main", "de l'argent", "un ordinateur portable", "des bijoux"]
VETEMENTS = ["un uniforme scolaire bleu", "une robe rouge", "un t-shirt jaune", "des habits traditionnels"]
AGES = list(range(4, 16))

# ─────────────────────────────────────────────────────────────────────────────
# 3. RÈGLES D'URGENCE
# ─────────────────────────────────────────────────────────────────────────────

def calculer_urgence(type_incident, heure, nb_signalements):
    """Calcule le niveau d'urgence de manière réaliste."""
    base = INCIDENTS[type_incident]["urgence_base"]
    niveaux = ["FAIBLE", "MOYEN", "ÉLEVÉ", "CRITIQUE"]
    idx = niveaux.index(base)

    # Aggravation selon l'heure (nuit = plus dangereux)
    if heure >= 22 or heure <= 5:
        idx = min(idx + 1, 3)

    # Aggravation selon nombre de signalements
    if nb_signalements >= 5:
        idx = min(idx + 1, 3)

    # Réduction si peu de signalements (incident mineur)
    if nb_signalements == 1 and type_incident in ["Vol", "Accident"]:
        idx = max(idx - 1, 0)

    # Petite randomisation ±1 niveau
    bruit = random.choices([-1, 0, 0, 1], weights=[0.1, 0.6, 0.2, 0.1])[0]
    idx = max(0, min(3, idx + bruit))

    return niveaux[idx]


def calculer_temps_intervention(niveau_urgence):
    """Temps d'intervention en minutes selon l'urgence."""
    params = {
        "CRITIQUE": (5, 15),
        "ÉLEVÉ":    (10, 25),
        "MOYEN":    (20, 40),
        "FAIBLE":   (35, 60),
    }
    mn, mx = params[niveau_urgence]
    return round(random.uniform(mn, mx), 1)


def calculer_statut(niveau_urgence, date):
    """Statut réaliste selon urgence et ancienneté."""
    jours_depuis = (datetime(2025, 5, 24) - date).days
    if jours_depuis > 30:
        return random.choices(["Résolu", "En cours"], weights=[0.90, 0.10])[0]
    elif niveau_urgence == "CRITIQUE":
        return random.choices(["Résolu", "En cours"], weights=[0.60, 0.40])[0]
    else:
        return random.choices(["Résolu", "En cours"], weights=[0.75, 0.25])[0]


# ─────────────────────────────────────────────────────────────────────────────
# 4. DISTRIBUTION TEMPORELLE RÉALISTE
# ─────────────────────────────────────────────────────────────────────────────

def generer_heure():
    """Génère une heure avec pics réalistes (matin 7-9h, soir 18-23h)."""
    poids_heures = [
        0.5, 0.3, 0.2, 0.2, 0.3, 0.5,   # 0h-5h (nuit calme)
        1.0, 3.0, 3.5, 2.5, 2.0, 2.5,   # 6h-11h (matinée active)
        2.0, 1.8, 2.0, 2.5, 3.0, 3.5,   # 12h-17h (après-midi)
        4.0, 4.5, 4.0, 3.5, 2.5, 1.5,   # 18h-23h (soirée = pic)
    ]
    return random.choices(range(24), weights=poids_heures)[0]


def generer_date():
    """Génère une date entre janvier 2024 et mai 2025."""
    debut = datetime(2024, 1, 1)
    fin   = datetime(2025, 5, 23)
    delta = (fin - debut).days
    return debut + timedelta(days=random.randint(0, delta))


def generer_description(type_incident, quartier, heure, nb_signalements):
    """Génère une description textuelle réaliste."""
    templates = INCIDENTS[type_incident]["descriptions"]
    tpl = random.choice(templates)
    desc = tpl.format(
        age=random.choice(AGES),
        lieu=quartier,
        duree=random.choice(["1h", "2h", "3h", "30 min", "4h", "ce matin"]),
        heure=heure,
        vetement=random.choice(VETEMENTS),
        temoin=nb_signalements,
        objet=random.choice(OBJETS),
    )
    return desc


# ─────────────────────────────────────────────────────────────────────────────
# 5. GÉNÉRATION PRINCIPALE
# ─────────────────────────────────────────────────────────────────────────────

def generer_dataset(n=3000):
    """Génère n alertes simulées réalistes."""
    print(f"🔄 Génération de {n} alertes réalistes pour le Cameroun...")

    villes      = list(GEOGRAPHIE.keys())
    poids_villes = [GEOGRAPHIE[v]["poids"] for v in villes]
    types_inc   = list(INCIDENTS.keys())
    poids_types  = [INCIDENTS[t]["poids"] for t in types_inc]

    alertes = []

    for i in range(n):
        # Sélection ville & quartier
        ville = random.choices(villes, weights=poids_villes)[0]
        info_ville = GEOGRAPHIE[ville]
        quartier = random.choice(list(info_ville["quartiers"].keys()))
        lat_q, lon_q = info_ville["quartiers"][quartier]

        # Légère variation GPS pour rendre la carte vivante
        lat = lat_q + random.uniform(-0.005, 0.005)
        lon = lon_q + random.uniform(-0.005, 0.005)

        # Sélection incident
        type_inc = random.choices(types_inc, weights=poids_types)[0]

        # Temporel
        date = generer_date()
        heure = generer_heure()
        minute = random.randint(0, 59)
        heure_str = f"{heure:02d}:{minute:02d}"

        # Signalements
        nb_signalements = random.choices(
            range(1, 13),
            weights=[30, 25, 15, 10, 7, 4, 3, 2, 1.5, 1, 0.8, 0.7]
        )[0]

        # Urgence, temps, statut
        urgence = calculer_urgence(type_inc, heure, nb_signalements)
        temps_interv = calculer_temps_intervention(urgence)
        statut = calculer_statut(urgence, date)

        # Description textuelle
        description = generer_description(type_inc, quartier, heure, nb_signalements)

        alertes.append({
            "ID_alerte":           f"SAI-{2024 + (date.year - 2024):04d}-{i+1:04d}",
            "Date":                date.strftime("%Y-%m-%d"),
            "Heure":               heure_str,
            "Heure_num":           heure,
            "Jour_semaine":        date.strftime("%A"),
            "Mois":                date.month,
            "Mois_nom":            date.strftime("%B"),
            "Annee":               date.year,
            "Region":              info_ville["region"],
            "Ville":               ville,
            "Quartier":            quartier,
            "Latitude":            round(lat, 6),
            "Longitude":           round(lon, 6),
            "Type_incident":       type_inc,
            "Description":         description,
            "Nombre_signalements": nb_signalements,
            "Niveau_urgence":      urgence,
            "Temps_intervention":  temps_interv,
            "Statut":              statut,
        })

    df = pd.DataFrame(alertes)
    print(f"✅ {len(df)} alertes générées.")
    return df


# ─────────────────────────────────────────────────────────────────────────────
# 6. SAUVEGARDE
# ─────────────────────────────────────────────────────────────────────────────

def sauvegarder(df):
    os.makedirs("data/raw",       exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    # Brut
    path_raw = "data/raw/alertes_cameroun_raw.csv"
    df.to_csv(path_raw, index=False, encoding="utf-8-sig")
    print(f"💾 Données brutes → {path_raw}")

    # Traité — même dataset ici (déjà propre)
    path_csv = "data/processed/alertes_cameroun_final.csv"
    df.to_csv(path_csv, index=False, encoding="utf-8-sig")
    print(f"💾 Données finales CSV → {path_csv}")

    # Parquet (optimisé pour le dashboard)
    path_parquet = "data/processed/alertes_cameroun_final.parquet"
    df.to_parquet(path_parquet, index=False)
    print(f"💾 Données finales Parquet → {path_parquet}")


def afficher_stats(df):
    print("\n" + "="*60)
    print("📊 STATISTIQUES DU DATASET GÉNÉRÉ")
    print("="*60)
    print(f"  Total alertes        : {len(df)}")
    print(f"  Période              : {df['Date'].min()} → {df['Date'].max()}")
    print(f"  Villes couvertes     : {df['Ville'].nunique()}")
    print(f"  Quartiers couverts   : {df['Quartier'].nunique()}")
    print(f"\n  Répartition par type d'incident :")
    for t, n in df['Type_incident'].value_counts().items():
        pct = 100 * n / len(df)
        print(f"    {t:<25} {n:>4} alertes ({pct:.1f}%)")
    print(f"\n  Répartition par niveau d'urgence :")
    for u, n in df['Niveau_urgence'].value_counts().items():
        pct = 100 * n / len(df)
        print(f"    {u:<12} {n:>4} alertes ({pct:.1f}%)")
    print(f"\n  Statut :")
    for s, n in df['Statut'].value_counts().items():
        pct = 100 * n / len(df)
        print(f"    {s:<12} {n:>4} ({pct:.1f}%)")
    print(f"\n  Temps d'intervention moyen : {df['Temps_intervention'].mean():.1f} min")
    print("="*60)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = generer_dataset(n=3000)
    sauvegarder(df)
    afficher_stats(df)
    print("\n✅ Génération terminée ! Prêt pour l'entraînement des modèles.")
