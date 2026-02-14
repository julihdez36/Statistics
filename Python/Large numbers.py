# -*- coding: utf-8 -*-
# Law of large numbers

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2131982)

# Ejemplo ley de grandes números
# moneda p=1/2 cara=1 seca=0

resultados = []

np.random.choice(['Heads','Tails'], 1)

for i in range(1,1000):
    lanzamientos = np.random.choice([0,1], i)
    caras = lanzamientos.mean() # Proporción de apairición de uno
    resultados.append(caras)



plt.plot(resultados, c = 'r')
plt.axhline(0.5)
plt.xlabel("Number of dice rolls")
plt.ylabel("Frequency of faces")
plt.grid(linestyle = '--')
plt.show()

