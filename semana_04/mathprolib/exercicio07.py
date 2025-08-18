import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('metrics.csv')

epoca = np.arange(1, len(data) + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,6))

ax1.plot(epoca, data['train_acc'], '-', label='Acurácia de Treino')
ax1.plot(epoca, data['val_acc'], '-', label='Acurácia de Validação')
ax1.set_xlabel('Épocas')
ax1.set_ylabel('Acurácia')
ax1.legend()
ax1.grid(True)

ax2.plot(epoca, data['train_loss'], '-', label='Loss de Treino')
ax2.plot(epoca, data['val_loss'], '-', label='Loss de Validação')
ax2.set_title('Histórico de Perda (Loss)')
ax2.set_xlabel('Épocas')
ax2.set_ylabel('Loss')
ax2.legend()
ax2.grid(True)

plt.tight_layout()

plt.show()