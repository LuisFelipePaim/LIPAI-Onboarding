from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('../pandas/datasets/classification_results_trial_0001.csv')

plt.scatter(
    data[data['real_class'] == data['predicted_class']]['prob_benign'], 
    data[data['real_class'] == data['predicted_class']]['prob_malign'], 
    c='grey',
    alpha=0.5,
    label='Acerto'    
)


plt.scatter(
    data[data['real_class'] != data['predicted_class']]['prob_benign'],
    data[data['real_class'] != data['predicted_class']]['prob_malign'],
    c='red',
    alpha=0.5,
    label='Erro'
)

plt.title('Dsipersão de Probabilidades')
plt.xlabel('Probabilidade de Ser Benigno')
plt.ylabel('Probabilidade de Ser Maligno')

plt.legend()

plt.axvline(x=0.5, color='grey', linestyle='--', linewidth=0.8)
plt.axhline(y=0.5, color='grey', linestyle='--', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.3)

plt.show()