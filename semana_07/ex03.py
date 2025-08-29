import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader

titanic = sns.load_dataset('titanic')

feature_names = ['pclass', 'female', 'age', 'fare']
titanic['female'] = titanic['sex'].map({'male': 0, 'female': 1})
titanic.dropna(subset=feature_names, inplace=True)  #891 para 714

X = titanic[feature_names].to_numpy()
y = titanic['survived'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state=123)

print('Tamanho de X_train: ', X_train.shape)
print('Tamanho de X_test: ', X_test.shape)
print('Tamanho de y_train: ', y_train.shape)
print('Tamanho de y_test: ', y_test.shape)

class ClassBin(nn.Module):
    # Construtor
    def __init__(self):
        super(ClassBin, self).__init__()
        self.fc1 = nn.Linear(4, 16) # primeira hidden layer
        self.fc2 = nn.Linear(16, 8) # segunda hidden layer
        self.fc3 = nn.Linear(8, 1) # terceira hidden layer
        self.sigmoid = nn.Sigmoid() # output layer com ativação Sigmoid

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        x = self.sigmoid(x)
        
        return x

model = ClassBin()

# print(model)

loss_fn = nn.BCELoss()
epochs = 100
batch_size = 32  # X_train 535 / 32 = 16.71 (então são 17 batches de 32)
learning_rate = 0.1

# Instânciar o Otimizador Adam
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Converter X e y para torch.Tensor
X_train = torch.Tensor(X_train)
y_train = torch.Tensor(y_train)
X_test = torch.Tensor(X_test)
y_test = torch.Tensor(y_test)

# Um Dataset de Tensores - Array [X, y]
train = TensorDataset(X_train, y_train)
train_loader = DataLoader(train, batch_size=batch_size, shuffle=True)

test = TensorDataset(X_test, y_test)
test_loader = DataLoader(test, batch_size=batch_size, shuffle=True)

for t in range(epochs):
    model.train() # Colocar o modelo em modo de treinamento (calcula os gradientes)
    
    # Batch Size
    for data in train_loader:
        # dar nome aos bois
        X = data[0]
        y = data[1]
        
        # Propagação (Feed Forward)
        y_pred = model(X)
    
        # Calcular erro usando a função-custo
        # y precisa virar um Tensor com tamanho (batch_size, 1)
        loss = loss_fn(y_pred, y.unsqueeze_(1))
        
        # Zera os gradientes antes da Retro-propagação (Backpropagation)
        model.zero_grad()

        # Retro-propagação (Backpropagation)
        loss.backward()

        # Atualização dos parâmetros
        optimizer.step()

    # Fim da Época
    print(f"""Época {t + 1},
          Custo Treino: {round(loss.item(), 3)}""")
    
model.eval() # coloca o modelo em modo de avaliação (sem calcular gradientes)

train_pred = model(X_train)
train_pred = train_pred.detach().apply_(lambda x : 1 if x > 0.5 else 0)
train_acc = torch.sum(train_pred.flatten() == y_train) / train_pred.size(0)

test_pred = model(X_test)
test_pred = test_pred.detach().apply_(lambda x : 1 if x > 0.5 else 0)
test_acc = torch.sum(test_pred.flatten() == y_test) / test_pred.size(0)

print(f"Acurácia de Treino: {train_acc}")
print('\n ---------------------------\n')
print(f"Loss: {loss}")
print('\n ---------------------------\n')
print(f"Acurácia de Teste: {test_acc}")