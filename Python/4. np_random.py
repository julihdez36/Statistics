# Random Number Generation module

import numpy as np
from numpy import random


random.random(size = 3) #  Uniformly distributed floats over [0, 1)

random.random(10)*100

random.randint(1,11)  #integers from low (inclusive) to high (exclusive)


random.randint(15,50, size = 100)

random.randint(15,50, size = (10,10))

# Select a random sample form a given 1-D array

A = random.random(20)

random.choice(A)

L = ['Luis','Rosa','Lili','Pedro']

random.choice(L)

L2= list(range(1,21))

random.choice(L2, size = [10,3])

A = random.choice(['A','B','C'], p = [.65,.25,.1], size = 1000)

np.unique(A, return_counts= True)[1] / len(A)

# Modify a sequence in-place by shuffling its contents.

random.shuffle(L), L

random.permutation(L) # Randomly permute a sequence

# Random number generation 

random.normal(loc = 1, scale = .5, size = 10)

import matplotlib.pyplot as plt

for i in [100000, 50]:
    A = random.normal(size = i)
    plt.hist(A, alpha = .5, density = True, label = f'{i} elements')
plt.legend()
plt.grid(linestyle = '--')
plt.show()

# Other probability distributions

random.binomial(n=1000,p=0.5,size=10000)

random.poisson(lam=10,size=1000)

random.uniform(110,size=(100))

logis = random.logistic(loc=1,scale=2,size=1000)
plt.hist(logis)

random.exponential(scale=0.1,size=100)
