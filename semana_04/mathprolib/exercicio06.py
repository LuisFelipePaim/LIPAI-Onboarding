from matplotlib import pyplot as plt
import pandas as pd

'''
Resposta:

Segundo os dados que temos, o tipo de erro mais comum é o falso negativo, 
esse também é o tipo de erro mais preocupante, haja visto que ele pode 
fazer com que o tratamento para aquela paciente que, no teste constou como
negativo, mas que na realidade ele é positivo possa demorar mais para ser 
iniciado, tendo em vista o resultado desse exame feito pelo modelo
'''

data = pd.read_csv('../pandas/datasets/classification_results_trial_0001.csv')

falso_negativo_count = data[(data['real_class'] == 'malign') & (data['predicted_class'] == 'benign')].shape[0]

falso_positivo_count = data[(data['real_class'] == 'benign') & (data['predicted_class'] == 'malign')].shape[0]


erros_cometidos = ['Falso Positivo', 'Falso Negativo']
contador_de_erros = [falso_positivo_count, falso_negativo_count]

plt.figure(figsize=(8,6))
barras = plt.bar(erros_cometidos, contador_de_erros, color=['#ff9999', '#66b3ff'])

plt.title('Erros Cometidos Pelo Modelo')
plt.ylabel('Número de Ocorrências')
plt.ylim(0, max(contador_de_erros) * 1.2)

for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2.0, yval + 0.1, int(yval), ha='center', va='bottom') 

plt.show()
