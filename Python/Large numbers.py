# -*- coding: utf-8 -*-

# Law of large numbers

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2131982)


resultados = []

np.random.choice(['Heads','Tails'], 5)

for i in range(1,10000):
    lanzamientos = np.random.choice([0,1], i)
    caras = lanzamientos.mean() # Proportion
    resultados.append(caras)



plt.plot(resultados, c = 'r', linewidth =.4)
plt.axhline(0.5)
plt.title('Law of large numbers')
plt.xlabel("Number of dice rolls")
plt.ylabel("Frequency of faces")
plt.grid(linestyle = '--')
plt.show()

