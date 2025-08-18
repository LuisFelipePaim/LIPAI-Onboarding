import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('../pandas/datasets/classification_results_trial_0001.csv')

plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(8, 7))


intervalos_gráfico = np.arange(0, 1.1, 0.1)

plt.hist(data['prob_benign'], bins=intervalos_gráfico,width=0.09, color="grey", edgecolor="white")

eixo_x = [f'({edge:.1f}-{intervalos_gráfico[i+1]:.1f})' for i, edge in enumerate(intervalos_gráfico[:-1])]
x_ticks =  [edge + 0.05 for edge in intervalos_gráfico[:-1]]
plt.xticks(x_ticks, eixo_x, rotation=45, ha='right')

plt.title("Histograma de Probabilidades de Ser Benigno")
plt.xlabel("Intervalo de Probabilidade")
plt.ylabel("Frequência")

plt.show()