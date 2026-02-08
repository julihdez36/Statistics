# Probabily sitribution

import numpy as np
from numpy import random
import seaborn as sns

x = random.normal(size = 1000)

sns.displot(x, kde = True);


x1=random.binomial(n=10,p=0.5,size=100000)
sns.displot(x1, kde = True);



sns.distplot(x1),sns.distplot(x)


x2=random.poisson(lam=2,size=100000)
sns.distplot(x2)


y1=random.binomial(n=1000,p=0.01,size=100000)
y2=random.poisson(lam=10,size=100000)
sns.displot(y1, color = 'r')
sns.displot(y2)

# https://www.youtube.com/watch?v=uial-2girHQ