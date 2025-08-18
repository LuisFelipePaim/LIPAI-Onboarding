import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../pandas/datasets/classification_results_trial_0001.csv')
'''
    Crie um gráfico de barras mostrando a 
    contagem de imagens para real_class 
    (quantas "benigno" e "maligno" são na realidade).
'''
malignos_bol = (data['real_class'] == 'malign')
malignos = data[malignos_bol]
malignos_qtd = malignos.shape[0] 

benignos_bol = (data['real_class'] == 'benign')
benignos = data[benignos_bol]
benignos_qtd = benignos.shape[0] 


categorias = ['Malignos', 'Benignos']
valores = [malignos_qtd, benignos_qtd]

plt.figure(figsize=(5,6))
plt.bar(categorias, valores, width=0.4, color='grey')
plt.yticks(range(0, 61, 5))


plt.title("Quantidade de Exames Malignos e Benignos")
plt.xlabel("Categorias")
plt.ylabel("Quantidade")
plt.grid()

plt.show()

