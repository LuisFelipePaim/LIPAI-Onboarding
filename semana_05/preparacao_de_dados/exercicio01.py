import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
    Esse código plota um gráfico que faz o cálculo do IMC de cada linha, e, após isso
    cria um histograma que possui em seu eixo X as faixas de IMC, e no eixo Y o número 
    de ocorrências.
'''


dataset = pd.read_csv('./datasets/obesidade.csv')
dataset['IMC'] = dataset['Weight'] / (dataset['Height'] ** 2)

plt.figure(figsize=(12, 7)) 

sns.histplot(
    data=dataset,
    x='IMC',
    binwidth=5,    
    binrange=(0, 55), 
    kde=True,      
    color='grey'   
)

plt.title('Distribuição do Índice de Massa Corporal (IMC)', fontsize=16)
plt.xlabel('IMC', fontsize=12)
plt.ylabel('Contagem (Frequência)', fontsize=12)
plt.xticks(np.arange(0, 56, 5)) 
plt.grid(axis='y', linestyle='--', alpha=0.7) 

plt.show()