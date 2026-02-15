# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Birthday paradox

def same_birthday(n = 23):
    p = 1
    for i in range(2, n+1):
        p *= (365 - i + 1)/365
    return 100* (1 - p)
        
same_birthday(n =50)

# Monty hall paradox

np.random.choice([0, 1, 2],1)

def simular_monty_hall(itr=100):
    ganadas_cambiando = 0
    ganadas_manteniendo = 0
    
    victorias = 0

    for _ in range(itr):
        doors = [0, 1, 2] # Las tres puertas
        premio = np.random.choice(doors,1)
        eleccion_inicial = np.random.choice(doors,1)
        
        if premio == eleccion_inicial:
            victorias += 1
    return victorias / itr
            
        
simular_monty_hall(itr = 1000)    
    
        
# Changing door


def simular_monty_hall(iteraciones=100000):
    ganadas_cambiando = 0
    ganadas_manteniendo = 0

    for _ in range(iteraciones):
        puertas = [0, 1, 2] # Las tres puertas
        premio = np.random.randint(0, 2) # El coche está detrás de una
        eleccion_inicial = np.random.randint(0, 2) # El concursante elige una

        # Monty abre una puerta que:
        # 1. No sea la que eligió el concursante
        # 2. No sea la que tiene el premio
        puertas_restantes = [p for p in puertas if p != eleccion_inicial and p != premio]
        puerta_abierta_por_monty = np.random.choice(puertas_restantes)

        # Si el concursante decide CAMBIAR:
        # Elige la puerta que no es la inicial ni la que abrió Monty
        cambio_eleccion = [p for p in puertas if p != eleccion_inicial and p != puerta_abierta_por_monty][0]

        # Contabilizar éxitos
        if eleccion_inicial == premio:
            ganadas_manteniendo += 1
        if cambio_eleccion == premio:
            ganadas_cambiando += 1

    return ganadas_manteniendo, ganadas_cambiando

# Ejecución
n = 100000
mantener, cambiar = simular_monty_hall(n)

print(f"Resultados tras {n} simulaciones:")
print(f"Ganaste manteniendo: {mantener} ({mantener/n:.2%})")
print(f"Ganaste cambiando: {cambiar} ({cambiar/n:.2%})")


