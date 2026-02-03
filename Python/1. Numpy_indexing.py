# Indexing


# ndarrays can be indexed using the standard Python x[obj] syntax,
# where x is the array and obj the selection. 

import numpy as np

x = np.arange(10)

x[2]

x.shape = (2,5)
x[1,3]

x[1,-1]

x[0]

x[0][2]

# Slicing and striding

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x[1:7:2]

x[-2:10]
x[-3:3:-1]

x[5:]

# https://numpy.org/doc/stable/user/basics.indexing.html