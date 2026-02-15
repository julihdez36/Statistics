# -*- coding: utf-8 -*-

'''
Metodos montecarlo. Los podemos utilizar para hacer simulaciones estocasticas

La idea es utilizar una simulacion estocastica para estimar el area de un 
circulo. A partir de ello, vamos a aproximar Pi

Qué haremos:
    Elegimos una entrada
    Elegimos una distribución de probabilidad
    Simulamos con un muestreo la distribución de probabilidad
    Realizar un calculo probabilistico del input simulado
    
Imaginemos un circulo de radio 1, r = 1
Por tanto el area, A = pi*r = pi
Area del cuadrado es 4

'''

import numpy as np

N = 100000 # numero de simulaciones

n_ci = 0 #Puntos en el circulo
n_cu = 0 #puntos en el cuadrado

l_x = []
l_y = []

for _ in range(N):
    x = np.random.uniform(-1,1)
    l_x.append(x)
    y = np.random.uniform(-1,1)
    l_y.append(y)
    
# Visualicemoslos

for i in range(N):
    normC=l_x[i]**2+l_y[i]**2
    if normC <= 1:
        n_ci+=1
    n_cu+=1
    
import matplotlib.pyplot as plt

for i in range(1000):
    normC=l_x[i]**2+l_y[i]**2
    if normC<=1:
        plt.plot(l_x[i],l_y[i],'o',color='blue')
    else:
        plt.plot(l_x[i],l_y[i],'o',color='red')


p=4*(n_ci/n_cu)

print(f'Aproximación estocastica a pi: {p}')
