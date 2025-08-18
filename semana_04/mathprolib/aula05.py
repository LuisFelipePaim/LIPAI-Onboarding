import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = x**2
y2 = x**5
'''
    Subplots
'''

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2 ,  figsize=(8, 4))
plt.suptitle("Gráficos com Subplots")

ax1.plot(x, y1)
ax2.plot(x, y2)
ax3.plot(x, y1)
ax4.plot(x, y2)


plt.show()