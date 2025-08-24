import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/hypothyroid.csv', na_values='?')

mean_age = df['age'].mean()
df['age'] = df['age'].fillna(mean_age)
teste = df['age'].isnull()

'''
    Apresentar histograma das idades presentes no dataset

'''
plt.figure(figsize=(12, 7))


intervalo_grafico = np.arange(0, 101, 10)
plt.hist(df['age'], bins=intervalo_grafico, width=9.5, color='grey', edgecolor='white')

eixo_x = [f'({edge:.1f} até {intervalo_grafico[i+1]:.1f} anos)' for i, edge in enumerate(intervalo_grafico[:-1])]
x_ticks = [edge + 10 for edge in intervalo_grafico[:-1]]
plt.xticks(x_ticks, eixo_x, rotation=45, ha='right')

plt.title('Histograma de distribuição de idade no Dataset')
plt.xlabel('Intervalo de Probabilidades')
plt.ylabel('Frequência')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() 

plt.show()