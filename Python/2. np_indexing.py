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

# Dimensional indexing tools

y = np.eye(5)

y[:2,:2] # (row,column)

z = np.random.random(12)*10
z.shape = (3,2,2)
z


z[1:2,:,:] # array
z[:,1:2,:] # row

# elipsis
z[..., 0], z[:,:,0]

# Excercises

'''
From each row, a specific element should be selected.
The row index is just [0, 1, 2] and the column index specifies 
the element to choose for the corresponding row, here [0, 1, 0].
 Using both together the task can be solved using advanced indexing:
'''

x = np.array([[1, 2], [3, 4], [5, 6]])

x[[0, 1, 2], [0, 1, 0]]

x[[2,1,0],[0,1,0]]

# Boolean array indexing

x[x > 2]

x = np.array([[1., 2.], [np.nan, 3.], [np.nan, np.nan]])
x[~np.isnan(x)]

x = np.array([1., -1., -2., 3])
x[x < 0] += 20
