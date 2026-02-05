'''
At the core of the NumPy package, is the array, called ndarray, object. 
This encapsulates n-dimensional arrays of homogeneous data types.

Vectorization: element-by-element operations 
'''

import numpy as np

# Array creation

# From another python object

a = np.array(list(range(2,5)))

# The type of the array can also be explicitly specified

b = np.array([i*2 for i in range(1,11)], dtype = float)
b

# Intrinsic numpy array creation functons

# 1D array

np. arange(1,20,2) #start, stop, step

np.linspace(0,2,9) # start, stop, num

# Linspace is useful when you can evaluate a function

x = np.linspace(0, 2*np.pi,100)
f = np.sin(x)

import matplotlib.pyplot as plt

plt.plot(f)


# 2D arrya creation

np.eye(2) # Identity matrix

np.diag([1,2,3]) # diagonal elements

np.vander(np.arange(1,6)) # vandermonde matrix


# General array creation functions

np.zeros([2,2])

np.ones([3,3])

np.random.default_rng(42).random((2,3)) # values between 0-1

np.random.default_rng(42).random((2,3,2)) # 3 dimensions

np.indices((3,3))


# Joining routines

A1 = np.ones([2,2])
A2 = np.ones([2,2])*2
A3 = np.ones([2,2])*3
A4 = np.ones([2,2])*4


np.block([[A1,A2],
         [A3,A4]])


####### More important attributes of an ndarray #######

a.ndim # number of axes or dimensions

a.shape #dimensions of the array. This is a tuple of integers

a.size # Total number of elements

a.dtype # type of element of the array







