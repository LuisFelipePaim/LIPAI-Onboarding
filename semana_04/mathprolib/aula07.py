from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 30)
y = np.cos(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, 
         color="r", 
         lw=0.5, 
         marker="o", 
         linestyle="dashdot")
plt.grid(True)
plt.title("Gráfico do Cosseno")
plt.xlabel("Eixo do Tempo")
plt.ylabel("Eixo da Amplitude")
plt.show()