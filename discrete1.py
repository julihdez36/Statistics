# Ecuación logística discreta

import numpy as np
import matplotlib.pyplot as plt

# Definimos tres condiciones iniciales

x0 = [.4,.6,1.3]

# Definimos la función

def f(r,x):
    return r*x*(1-x)

T = np.arange(0,1.01,0.01)
T

# Grafiquemos formas de la función para distintas r

for i in [.1,1,1.01,1.5,2.5]:
    plt.plot(T,f(i,T), label = f'r = {i}' )
    plt.legend()
plt.grid(linestyle = '--')
plt.show()


for i in [.1,.6,1,1.01,1.5,2,2.5,3]:
    plt.plot(T,f(i,T), label = f'$r = {i}$' )
    plt.legend()
plt.plot(T,T, label = '$f(x)=x$')
plt.grid(linestyle = '--')
plt.show()

# Hagamos el diagrama de la telaraña (cobweb) en aplicación losgitica

def cobweb(r, T, f):
    plt.plot(T,f(r,T), label = f'r = {r}')
    plt.plot(T,T, label = '$f(x) = x$')
    xc = 0.05
    for i in range(50):
        plt.plot([xc,xc],[xc,f(r,xc)], color = 'k', linestyle = '--')
        plt.plot([f(r,xc),xc],[f(r,xc),f(r,xc)], color = 'k', linestyle='--')
        xc = f(r,xc)
    plt.grid(linestyle = '--')
    plt.legend()
    plt.show()

cobweb(r = 2.5,T = T,f = f)

# Grafiquemos ahora el sistema dinámico

x = [.05]
r = 1.5
for i in range(100):
    x.append(f(r,x[-1]))

plt.plot(x,'.')
