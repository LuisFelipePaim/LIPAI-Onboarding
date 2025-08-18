from matplotlib import pyplot as plt
import pandas as pd

'''
    Crie outro gráfico de barras mostrando a 
    contagem de imagens para predicted_class 
    (quantas "benigno" e "maligno" o modelo previu).
'''

data = pd.read_csv('../pandas/datasets/classification_results_trial_0001.csv')

malignosp_bol = (data['predicted_class'] == 'malign')
malignos_pre = data[malignosp_bol]
malignos_pre_qtd = malignos_pre.shape[0]

benignosp_bol = (data['predicted_class'] == 'benign')
benignos_pre = data[benignosp_bol]
benignos_pre_qtd = benignos_pre.shape[0]

categorias = ['Malignos', 'Benignos']
valores = [malignos_pre_qtd, benignos_pre_qtd]

plt.figure(figsize=(5,6))
plt.bar(categorias, valores, width=0.4, color='grey')
plt.yticks(range(0, 61, 5))

plt.title("Quantidade de Predições do Modelo")
plt.xlabel("Categorias")
plt.ylabel("Quantidade")
plt.grid()

plt.show()

