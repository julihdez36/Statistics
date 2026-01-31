# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 22:22:32 2026

@author: Julian
"""

# Fundamentals ---
 
import numpy as np

# Array creation

# 1. Using python sequences

a1D = np.array(list(range(1,5)))
a2D = np.array([[1, 2], [3, 4]])
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# 2. Intrinsic Numpy array creation functions

## 1D array creation functions
np.arange(10) # (start, stop, step)

np.linspace(1,4,6) # (start, stop, num)

## 2D array creation functions

np.eye(3) # Identity matrix

np.eye(3,5) # It changes size

#np. diag

np.diag([1,2,3])  # construct a diagonal array.
np.diag([1,2,3],2) 

np.diag(a2D) #Extract a diagonal array.

# Vandermonde matrix

np.vander(np.linspace(0, 2, 5), 2)
