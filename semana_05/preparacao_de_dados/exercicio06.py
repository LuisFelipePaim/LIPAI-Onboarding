import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./datasets/hypothyroid.csv')
 

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.dropna(axis=1, how='all', inplace=True)

df_numero = df.select_dtypes(include=np.number)

random_state = 42
amostra_10 = df_numero.sample(frac=0.1, random_state=random_state)
amostra_30 = df_numero.sample(frac=0.3, random_state=random_state)
amostra_50 = df_numero.sample(frac=0.5, random_state=random_state)

desc_orig = df_numero.describe()
desc_10 = amostra_10.describe()
desc_30 = amostra_30.describe()
desc_50 = amostra_50.describe()

colunas_pr = ['age', 'bgr', 'sc', 'hemo']
desc_orig_filtered = desc_orig[colunas_pr]
desc_10_filtered = desc_10[colunas_pr]
desc_30_filtered = desc_30[colunas_pr]
desc_50_filtered = desc_50[colunas_pr]

metricas = ['mean', 'std', 'min', '25%', '50%', '75%', 'max']
df_comparacao = pd.concat(
    [desc_orig_filtered.loc[metricas], desc_10_filtered.loc[metricas], 
     desc_30_filtered.loc[metricas], desc_50_filtered.loc[metricas]],
    keys=['Original', 'Amostra 10%', 'Amostra 30%', 'Amostra 50%'],
    axis=0 
)

print("Comparação das Métricas Estatísticas para Colunas Selecionadas:")
print(df_comparacao)

print("\nGerando gráfico para a distribuição de Idade (age)...")
plt.figure(figsize=(12, 7))
sns.kdeplot(df_numero['age'].dropna(), label='Original', linewidth=2.5, bw_adjust=0.5)
sns.kdeplot(amostra_10['age'].dropna(), label='Amostra 10%', linestyle='--', bw_adjust=0.5)
sns.kdeplot(amostra_30['age'].dropna(), label='Amostra 30%', linestyle='-.', bw_adjust=0.5)
sns.kdeplot(amostra_50['age'].dropna(), label='Amostra 50%', linestyle=':', bw_adjust=0.5)
plt.title('Comparação da Distribuição da Idade (age) entre Amostras')
plt.xlabel('Idade')
plt.ylabel('Densidade')
plt.legend()
plt.grid(True)
plt.show()

print("\nGerando gráfico para a distribuição de Glicemia (bgr)...")
plt.figure(figsize=(12, 7))
sns.kdeplot(df_numero['bgr'].dropna(), label='Original', linewidth=2.5, bw_adjust=0.5)
sns.kdeplot(amostra_10['bgr'].dropna(), label='Amostra 10%', linestyle='--', bw_adjust=0.5)
sns.kdeplot(amostra_30['bgr'].dropna(), label='Amostra 30%', linestyle='-.', bw_adjust=0.5)
sns.kdeplot(amostra_50['bgr'].dropna(), label='Amostra 50%', linestyle=':', bw_adjust=0.5)
plt.title('Comparação da Distribuição da Glicemia (bgr) entre Amostras')
plt.xlabel('Glicemia (bgr)')
plt.ylabel('Densidade')
plt.legend()
plt.grid(True)
plt.show()