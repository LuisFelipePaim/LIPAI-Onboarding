import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('./datasets/obesidade.csv')

plt.rcParams['font.family'] = 'Times New Roman'
plt.style.use('ggplot')

df['IMC'] = df['Weight'] / (df['Height'] ** 2)

imc_baixo = (df['IMC'] < 18.5)
imc_regular = (df['IMC'] >= 18.5) & (df['IMC'] < 25)
imc_alto = (df['IMC'] >= 25)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 10), constrained_layout=True)
fig.suptitle("Análise de IMC e histórico de sobrepeso na família", fontsize=20)

plot_configs = [
    {'title': 'IMC Baixo', 'data': df[imc_baixo]},
    {'title': 'IMC Regular', 'data': df[imc_regular]},
    {'title': 'IMC Alto', 'data': df[imc_alto]},
    {'title': 'Geral', 'data': df} 
]

for config, subplot_ax in zip(plot_configs, ax.flatten()):
    sns.countplot(
        x='family_history_with_overweight',
        data=config['data'],
        order=['yes', 'no'],
        palette=['#3498db', '#e74c3c'],
        width=0.4,
        ax=subplot_ax
    )
    subplot_ax.set_title(config['title'])
    subplot_ax.set_xlabel('Histórico Familiar')
    subplot_ax.set_ylabel('Ocorrências')
    subplot_ax.set_xticklabels(['Sim', 'Não'])

media_altura = df['Height'].mean()
media_peso = df['Weight'].mean()
media_imc = df['IMC'].mean()

print(f'Média de altura: {media_altura:.2f}')
print(f'Média de peso: {media_peso:.2f}')
print(f'Média de IMC: {media_imc:.2f}')

plt.show()

