from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('../pandas/datasets/classification_results_trial_0001.csv')

plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(8, 7))

intervalos_graficos = np.arange(0, 1.1, 0.1)

plt.hist(data['prob_benign'], bins=intervalos_graficos, width=0.09, color="grey", edgecolor="white")

eixo_x = [f'({edge:.1f}-{intervalos_graficos[i+1]:.1f})' for i, edge in enumerate(intervalos_graficos[:-1])]
x_ticks = [edge + 0.05 for edge in intervalos_graficos[:-1]]
plt.xticks(x_ticks, eixo_x, rotation=45, ha='right')

plt.title("Histograma de Probabilidades de Ser Maligno", fontsize=16)
plt.xlabel("Intervalo de Probabilidade", fontsize=13)
plt.ylabel("Frequência", fontsize=13)

plt.show()