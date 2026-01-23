#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
# Question 4
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r",encoding='utf-8') as fichier:
    contenu = pd.read_csv(fichier)

# Question 5
data = pd.DataFrame(contenu)
print(data)

# Question 6
nombre_lignes = len(contenu)
print('Le nombre de ligne est égal à ', nombre_lignes)
nombre_colonnes = contenu.shape[1]
print("Le nombre de colonnes est égal à ", nombre_colonnes)

# Question 7
print("Le type de chaque colonne est :")
print(contenu.dtypes)

# Question 8
print("Le nom des colonnes est")
print(contenu.columns)

#Question 9 
inscrits = contenu["Inscrits"]
print("Le nombre des inscrits est:")
print(inscrits)

# Question 10
types_colonnes = {col: str(contenu[col].dtype) for col in contenu.columns}
somme_colonnes = []  # liste des résultats

for col in contenu.columns:
    # On regarde si le type est numérique
    if contenu[col].dtype in ["int64", "float64"]:
        somme = contenu[col].sum()
        somme_colonnes.append((col, somme))
print("\n=== Effectifs de chaque colonne ===")
for nom, total in somme_colonnes:
    print(f"{nom:30s} : {total}")

#Question 11
import matplotlib.pyplot as plt
import os

# créer le dossier s’il n'existe pas
os.makedirs("img_barres", exist_ok=True)

for idx, row in contenu.iterrows():
    departement = row["Libellé du département"]
    inscrits = row["Inscrits"]
    votants = row["Votants"]

    plt.figure(figsize=(6, 4))
    plt.bar(["Inscrits", "Votants"], [inscrits, votants], color=["blue", "green"])
    plt.title(f"Inscrits / Votants - {departement}")
    plt.ylabel("Effectifs")

    filename = f"img_barres/{departement.replace('/', '-')}.png"
    plt.savefig(filename, dpi=150)
    plt.close()

# Question 12
os.makedirs("img_circulaires", exist_ok=True)

for idx, row in contenu.iterrows():
    departement = row["Libellé du département"]

    valeurs = [
        row["Blancs"],
        row["Nuls"],
        row["Exprimés"],
        row["Abstentions"]
    ]

    labels = ["Blancs", "Nuls", "Exprimés", "Abstentions"]

    plt.figure(figsize=(6, 6))
    plt.pie(valeurs, labels=labels, autopct="%1.1f%%")
    plt.title(f"Répartition des votes - {departement}")

    filename = f"img_circulaires/{departement.replace('/', '-')}.png"
    plt.savefig(filename, dpi=150)
    plt.close()

# Question 13
plt.figure(figsize=(8, 5))
plt.hist(contenu["Inscrits"], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution des inscrits")
plt.xlabel("Nombre d'inscrits")
plt.ylabel("Fréquence")
plt.savefig("histogramme_inscrits.png", dpi=150)
plt.close()

