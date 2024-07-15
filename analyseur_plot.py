"""
Created by Tchane821 - 2024
For analyse data with graphics
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# DEF VALUES
SEUIL_VITESSE = 1.0
SEUIL_FORCE = 15.0

print("Analyse plot start... pls wait")

csv_file_source = "./csv"
graph_file_source = "./graph"
csv_files = ["{csv_file_source}/{fn}" for fn in os.listdir(csv_file_source)]

for csv_file in csv_files:
    df = pd.read_csv(csv_file, sep=';')
    # print(df.head())
    # print(df.dtypes)

    # Filter)
    df = df[abs(df['vitesse']) > SEUIL_VITESSE]  # speed < 0.1 => delete
    df = df[abs(df['force']) > SEUIL_FORCE]  # torque < 2.0 => delete

    # Tracer les graphiques
    plt.figure(figsize=(12, 8), dpi=200)

    # Graphique de la Force
    plt.subplot(3, 1, 1)
    plt.plot(df['position'], df['force'], marker='o', linestyle='-', color='r')
    plt.title('Force en fonction de la Position')
    plt.xlabel('Position')
    plt.ylabel('Force')
    plt.grid(True)

    # Graphique de la Vitesse
    plt.subplot(3, 1, 2)
    plt.plot(df['position'], df['vitesse'], marker='o', linestyle='-', color='g')
    plt.title('Vitesse en fonction de la Position')
    plt.xlabel('Position')
    plt.ylabel('Vitesse')
    plt.grid(True)

    # Graphique de la Force et de la Vitesse
    plt.subplot(3, 1, 3)
    plt.plot(df['position'], df['force'], marker='o', linestyle='-', color='r', label='Force')
    plt.plot(df['position'], df['vitesse'], marker='o', linestyle='-', color='g', label='Vitesse')
    plt.title('Force et Vitesse en fonction de la Position')
    plt.xlabel('Position')
    plt.ylabel('Valeur')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()  # Pour éviter que les étiquettes des axes ne se chevauchent
    # plt.show()
    plt.savefig("{graph_file_source}/graph_{(csv_file.split('/')[-1])[5:]}.png")

print("Analyse plot fini !")
