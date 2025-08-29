import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

try:
    dados = pd.read_csv('./datasets/fitness_dataset.csv')
    
    dados['smokes'] = dados['smokes'].astype(str).replace({'1': 'yes', '0': 'no'})

    features = dados.drop('is_fit', axis=1)
    alvo = dados['is_fit']

    features_numericas = features.select_dtypes(include=['int64', 'float64']).columns
    features_categoricas = features.select_dtypes(include=['object']).columns

    transformador_numerico = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    transformador_categorico = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessador = ColumnTransformer(
        transformers=[
            ('num', transformador_numerico, features_numericas),
            ('cat', transformador_categorico, features_categoricas)
        ])

    features_treino, features_teste, alvo_treino, alvo_teste = train_test_split(
        features, alvo, test_size=0.2, random_state=42, stratify=alvo
    )

    modelo_reg_logistica = Pipeline(steps=[
        ('preprocessador', preprocessador),
        ('classificador', LogisticRegression(random_state=42))
    ])
    modelo_reg_logistica.fit(features_treino, alvo_treino)
    previsoes_reg_logistica = modelo_reg_logistica.predict(features_teste)

    modelo_arvore = Pipeline(steps=[
        ('preprocessador', preprocessador),
        ('classificador', DecisionTreeClassifier(random_state=42))
    ])
    modelo_arvore.fit(features_treino, alvo_treino)
    previsoes_arvore = modelo_arvore.predict(features_teste)

    modelo_random_forest = Pipeline(steps=[
        ('preprocessador', preprocessador),
        ('classificador', RandomForestClassifier(random_state=42))
    ])
    modelo_random_forest.fit(features_treino, alvo_treino)
    previsoes_random_forest = modelo_random_forest.predict(features_teste)

    print("\n\n--- Desempenho dos Modelos no Conjunto de Teste ---")

    print("\nResultados para Regressão Logística:")
    print(f"Acurácia: {accuracy_score(alvo_teste, previsoes_reg_logistica):.4f}")
    print(classification_report(alvo_teste, previsoes_reg_logistica))

    print("\nResultados para Árvore de Decisão:")
    print(f"Acurácia: {accuracy_score(alvo_teste, previsoes_arvore):.4f}")
    print(classification_report(alvo_teste, previsoes_arvore))

    print("\nResultados para Random Forest:")
    print(f"Acurácia: {accuracy_score(alvo_teste, previsoes_random_forest):.4f}")
    print(classification_report(alvo_teste, previsoes_random_forest))

except FileNotFoundError:
    print("Erro: O arquivo 'fitness_dataset.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")