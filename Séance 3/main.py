#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023
#Séance 3

#Question 4
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as f : df = pd.read_csv(f)

#Question 5
colonnes_quantitatives = df.select_dtypes(include=["int64", "float64"])
moyennes = colonnes_quantitatives.mean()
moyennes = moyennes.round(2)
medianes = colonnes_quantitatives.median()
medianes = medianes.round(2)
modes = colonnes_quantitatives.mode().iloc[0]
modes = modes.round(2)
ecarts_types = colonnes_quantitatives.std()
ecarts_types = ecarts_types.round(2)
ecarts_absolus = (colonnes_quantitatives - moyennes).abs().mean()
ecarts_absolus = ecarts_absolus.round(2)
etendues = colonnes_quantitatives.max() - colonnes_quantitatives.min()
etendues = etendues.round(2)

#Question 6
print("Moyennes :", moyennes)
print("Médianes :", medianes)
print("Modes :", modes)
print("Écarts-types :", ecarts_types)
print("Écarts absolus à la moyenne", ecarts_absolus)
print("Étendues :", etendues)

#Question 7
# Distance interquartile (IQR)
iqr = colonnes_quantitatives.quantile(0.75) - colonnes_quantitatives.quantile(0.25)

# Distance interdécile (IDR)
idr = colonnes_quantitatives.quantile(0.9) - colonnes_quantitatives.quantile(0.1)
iqr = iqr.round(2)
idr = idr.round(2)
print("Distance interquartile:", iqr)
print("Distance interdécile:", idr)

#Question 8
for colonne in colonnes_quantitatives.columns:
    plt.figure(figsize=(6, 4))             
    plt.boxplot(colonnes_quantitatives[colonne].dropna())  
    plt.title(f"Boîte à moustaches - {colonne}")
    plt.ylabel(colonne)
    chemin = f"img/boxplot_{colonne}.png"
    plt.savefig(chemin)
    plt.close()   

#Question 9
df_islands = pd.read_csv("./data/island-index.csv", low_memory=False)

#Question 10
surfaces = df_islands["Surface (km²)"]
bornes = [0, 10, 25, 50, 100, 2500, 5000, 10000, float("inf")]
labels = [
    "]0, 10]",
    "]10, 25]",
    "]25, 50]",
    "]50, 100]",
    "]100, 2500]",
    "]2500, 5000]",
    "]5000, 10000]",
    "≥ 10000"
]
df_islands["Categorie_surface"] = pd.cut(surfaces, bins=bornes, labels=labels, right=True)
denombrement = df_islands["Categorie_surface"].value_counts().sort_index()

print("Dénombrement des catégories de surface :")
print(denombrement)
