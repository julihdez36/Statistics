
# Simulación Monte Carlo de portafolio de inversión



import numpy as np
import matplotlib.pyplot as plt

np.random.normal(0.07,0.04,(20,100))

100000*(1+np.random.normal(0.07,0.04,(20,100))).cumprod(axis=0)

def simula_port(inicial,rt,vl,t,s):
    np.random.seed(42)
    ret=np.random.normal(rt,vl,(t,s))
    valor_port=inicial*(1+ret).cumprod(axis=0)
    #figura
    plt.figure()
    plt.plot(valor_port,alpha=0.5)
    plt.title('Portafolio de inversión vía MonteCarlo')
    plt.xlabel(r'Año')
    plt.ylabel('Valor ($)')
    plt.grid(linestyle = '--')

    mejor_caso=valor_port.max(axis=1)[-1]
    peor_caso=valor_port.min(axis=1)[-1]
    plt.text(t/2, mejor_caso/2,f'Mejor caso : ${mejor_caso:.0f} '+f'\nPeor caso : ${peor_caso:.0f}',
             bbox=dict(facecolor='grey',alpha=0.6))
    plt.show()

simula_port(inicial=100000,rt=0.07,vl=0.1,t=15,s=100)
