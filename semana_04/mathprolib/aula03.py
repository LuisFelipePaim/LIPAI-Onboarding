import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
c = np.cos(x)
s = np.sin(x)

plt.figure("Gráficos consenoidais", figsize=(8,4))
plt.subplots_adjust(
    left   = 0.120,
    right  = 0.964,
    top    = 0.900,
    bottom = 0.140,
    wspace = 0.438,
    hspace = 0.736
)

ax1 = plt.subplots(2, 1, 1)
plt.plot(x, c)
ax1.set_title("Gráfico do Cosseno")
ax1.set_xlabel("Eixo de Tempo")
ax1.set_ylabel("Eixo de Amplitude")

ax2 = plt.subplots(2, 1, 2)
plt.plot(x, s)
ax2.set_title("Gráfico do Seno")
ax2.set_xlabel("Eixo de Tempo")
ax2.set_ylabel("Eixo de Amplitude")


plt.show()