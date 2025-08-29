import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader

# Define uma semente para reprodutibilidade
torch.manual_seed(123)

titanic = sns.load_dataset('titanic')

feature_names = ['pclass', 'female', 'age', 'fare']
titanic['female'] = titanic['sex'].map({'male': 0, 'female': 1})
titanic.dropna(subset=feature_names, inplace=True)

X = titanic[feature_names].to_numpy()
y = titanic['survived'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state=123)

print('--- Treinando com batch_size = 512 ---')
print('Tamanho de X_train: ', X_train.shape)
print('Tamanho de X_test: ', X_test.shape)
print('Tamanho de y_train: ', y_train.shape)
print('Tamanho de y_test: ', y_test.shape)
print('--------------------------------------\n')

class ClassBin(nn.Module):
    # Construtor
    def __init__(self):
        super(ClassBin, self).__init__()
        self.linear1 = nn.Linear(4, 4)
        self.dropout1 = nn.Dropout(0.2)
        self.linear2 = nn.Linear(4, 4)
        self.dropout2 = nn.Dropout(0.2)
        self.linear3 = nn.Linear(4, 1)
        self.dropout3 = nn.Dropout(0.2)
        self.sigmoid = nn.Sigmoid()

    # Propagação (Feed Forward)
    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.dropout1(x)
        x = F.relu(self.linear2(x))
        x = self.dropout2(x)
        x = F.relu(self.linear3(x))
        x = self.dropout3(x)
        x = self.sigmoid(x)
        return x

model = ClassBin()

loss_fn = nn.BCELoss()
epochs = 100
# ######################################
# # ALTERAÇÃO PRINCIPAL AQUI          ##
# ######################################
batch_size = 512
# ######################################
learning_rate = 0.1

# Instanciar o Otimizador SGD
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# Converter X e y para torch.Tensor
X_train = torch.Tensor(X_train)
y_train = torch.Tensor(y_train)
X_test = torch.Tensor(X_test)
y_test = torch.Tensor(y_test)

# Criar Datasets e DataLoaders
train = TensorDataset(X_train, y_train)
train_loader = DataLoader(train, batch_size=batch_size, shuffle=True)

test = TensorDataset(X_test, y_test)
test_loader = DataLoader(test, batch_size=batch_size, shuffle=True)

for t in range(epochs):
    model.train()
    for data in train_loader:
        X_batch = data[0]
        y_batch = data[1]

        y_pred = model(X_batch)
        loss = loss_fn(y_pred, y_batch.unsqueeze(1))
        
        model.zero_grad()
        loss.backward()
        optimizer.step()

# Coloca o modelo em modo de avaliação
model.eval()

# Calcula a acurácia no conjunto de treino
train_pred = model(X_train)
train_pred = (train_pred > 0.5).float()
train_acc = (train_pred.flatten() == y_train).float().mean()


# Calcula a acurácia no conjunto de teste
test_pred = model(X_test)
test_pred = (test_pred > 0.5).float()
test_acc = (test_pred.flatten() == y_test).float().mean()


print(f"Acurácia de Treino: {train_acc.item()}")
print('\n---------------------------\n')
print(f"Loss final: {loss.item()}")
print('\n---------------------------\n')
print(f"Acurácia de Teste: {test_acc.item()}")