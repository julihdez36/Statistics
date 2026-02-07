
# Broadcasting

'''
The term broadcasting describes how NumPy treats arrays with different shapes during
 arithmetic operations. Subject to certain constraints, the smaller array is 
 “broadcast” across the larger array so that they have compatible shapes.
'''

import numpy as np

# In the simplest case, the two arrays must have exactly the same shape

a = np.arange(1,4,dtype = float)
b = np.repeat(2, 3).astype(float)

a.shape == b.shape
a*b

# The simplest broadcasting example: an array and a scalar value

a*2

# You can add 1-d array to a 2-d array

a = np.repeat(np.arange(4, dtype = float), 3).reshape(4,3)*10
a

b = np.arange(1,4,dtype = float)
b

a+b # b is added to each row of a

b+a


# A practical example: vector quantization

from numpy import array, argmin, sqrt, sum

observation = array([111.0, 188.0])
codes = array([[102.0, 203.0],
               [132.0, 193.0],
               [45.0, 155.0],
               [57.0, 173.0]])
diff = codes - observation    # the broadcast happens here

dist = sqrt(sum(diff**2,axis=-1)) # finding the closets point
codes[argmin(dist)]  #shotest distance

import matplotlib.pyplot as plt

plt.figure(figsize = (8,6))
plt.scatter(codes[:,0],codes[:,1])
plt.scatter(observation[0], observation[1], c='red')

for i in range(codes.shape[0]):
    mi_color = 'red' if i == argmin(dist) else 'black'
    plt.plot([observation[0],codes[i,0]],
             [observation[1],codes[i,1]],linestyle = '--', 
             c = mi_color)

plt.grid(linestyle = '--')
plt.title("Euclidean distance for Broadcasting")
plt.show()
