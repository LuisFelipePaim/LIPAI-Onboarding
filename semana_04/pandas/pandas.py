import pandas as pd

''' -----------------------------------------------
    ----- Mostrar imagens malignas e benignas -----
    -----------------------------------------------
''' 
data = pd.read_csv('./datasets/classification_results_trial_0001.csv')
malignos_reais = (data['real_class'] == 'malign')
benignos_reais = (data['real_class'] == 'benign')
print('Mostrar a quantidade de imagens que são malignas e benignas.')
print(f'O nímero de imagens malignas é: {data[malignos_reais].shape[0]}')
print(f'O número de imagens benignas é: {data[benignos_reais].shape[0]}\n')   

''' -----------------------------------------------------------------------
    ----- Mostrar a quantidade de vezes que o modelo errou a predição -----
    ----------------------------------------------------------------------- 
''' 

# Gera uma series de booleans, onde os locais em que os valores da coluna real_class e predicted_class são diferentes o valor é true
data_erros_bol = data['real_class'] != data['predicted_class']

# Utilizo a series para filtrar e criar um dataframe contendo apenas as linhas em que as colunas real_class e predicted_class são diferentes
data_erros = data[data_erros_bol]
print('Mostrar a quantidade de vezes que o modelo errou a predição')
print(f'O número de vezes que o modelo errou foram: {data_erros.shape[0]}\n') 

''' ----------------------------------------------------------------------------------------------
    ----- Mostrar a confiança do modelo em suas predições, mesmo quando essas estavam erradas-----
    ----------------------------------------------------------------------------------------------
''' 

confianca_geral_maligno = (data['predicted_class'] == 'benign') & (data['prob_benign'] > data['prob_malign'])
confianca_geral_benigno = (data['predicted_class'] == 'malign') & (data['prob_benign'] < data['prob_malign'])

data_confianca_geral_mal = data[confianca_geral_maligno]
data_confianca_geral_ben = data[confianca_geral_benigno]
data_erros_benigno_bol = (data_erros['predicted_class'] == 'benign') & (data['prob_benign'] > data['prob_malign'])
data_confianca_erro_benigno = data_erros[data_erros_benigno_bol]

data_erros_maligno_bol = (data_erros['predicted_class'] == 'malign') & (data['prob_malign'] > data['prob_benign'])
data_confianca_erro_maligno = data_erros[data_erros_maligno_bol]

confianca_geral = data_confianca_geral_ben.shape[0] + data_confianca_geral_mal.shape[0]
confianca_erros = data_confianca_erro_benigno.shape[0] + data_confianca_erro_maligno.shape[0]

print(f'O número de vezes que o modelo estava confiante em geral foram: {confianca_geral}')
print(f'O número de vezes que o modelo estava confiante quando errou foram: {confianca_erros}')


'''
    ------------------------------------------------------------------
    ----------------------------Calcule:------------------------------
    ---Verdadeiros Positivos (TP) - real maligno, previsto maligno.---
    ----Verdadeiros Negativos (TN) - real benigno, previso benigno.---
    ------Falsos Positivos (FP) - real benigno, previsto maligno.-----
    ------Falsos Negativos (FN) - real maligno, previsto benigno.-----
    ------------------------------------------------------------------
'''

tp_bol = (data['real_class'] == 'malign') & (data['predicted_class'] == 'malign')
tp_data = data[tp_bol]

tn_bol = (data['real_class'] == 'benign') & (data['predicted_class'] == 'benign')
tn_data = data[tn_bol]

fp_bol = (data['real_class'] == 'benign') & (data['predicted_class'] == 'malign')
fp_data = data[fp_bol]

fn_bol = (data['real_class'] == 'malign') & (data['predicted_class'] == 'benign')
fn_data = data[fn_bol]


registros_tp = tp_data.shape[0]
registros_tn = tn_data.shape[0]
registros_fp = fp_data.shape[0]
registros_fn = fn_data.shape[0]

print(f'Verdadeiros positivos: {registros_tp}')
print(f'Verdadeiros negativos: {registros_tn}')
print(f'Falsos positivos: {registros_fp}')
print(f'Falsos negativos: {registros_fn}\n')

'''
    -------------------------------------------
    -----------Calculando acurácia-------------
    ------Acurácia: (TP+TN)/(TP+TN+FP+FN)------
    -------------------------------------------
'''


acuracia = (registros_tp + registros_tn)/(registros_tp + registros_tn + registros_fp + registros_fn)
print(f'Acuracia do Modelo: {acuracia:.2}')

precisao = registros_tp/(registros_tp + registros_fp)
print(f'Precisão do Modelo: {precisao:.2}')

recall = registros_tp/(registros_tp + registros_fn)
print(f'Recall do Modelo: {recall:.2}')

especificidade = registros_tn/(registros_tn + registros_fp) 
print(f'Especificade do Modelo: {especificidade:.2}\n')

'''
    -------------------------------------------
    ---Encontre as 5 imagens "benigno" com a---
    --menor probabilidade de serem "benigno"---
    --(prob_benign). O que isso pode indicar?--
    -------------------------------------------
    !!!Respostas dessa e da próxima pergunta no
    arquivo 'respostas.txt'!!!
'''

data_ord_proben = data[benignos_reais].sort_values(by=['prob_benign'], ascending=[True])
print(f'Cinco imagens benigno com a menor probabilidade de serem benignas')
print(f'{data_ord_proben['prob_benign'].head(5).reset_index(drop=True)}\n')
'''
    --------------------------------------------------
    ---Encontre as 5 imagens "maligno" com a maior----
    ---probabilidade de serem "benigno" (prob_benign)-
    -------------O que isso pode indicar?-------------
    --------------------------------------------------
'''

data_ord_promal = data[malignos_reais].sort_values(by=['prob_benign'], ascending=[False])
print(f'Cinco imagens malignas com a maior probabilidade de serem benignas')
print(f'{data_ord_promal['prob_benign'].head(5).reset_index(drop=True)}') 