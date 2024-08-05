import numpy as np


arr1 = np.array([1, 2, 3, 5, 6, 7])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

arr3 = np.zeros((2,3))
print(arr3)

arr4 = np.ones((3, 3))
"""
Output will be
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]"""
print(arr4)

arr5 = np.identity(5) 
""" identity in array will give you diagonaly 1
   [1. 0. 0. 0. 0.]
   [0. 1. 0. 0. 0.]
   [0. 0. 1. 0. 0.]
   [0. 0. 0. 1. 0.]
   [0. 0. 0. 0. 1.]]"""
print(arr5)

arr6 = np.arange(10)
""" Ouput will be
[0 1 2 3 4 5 6 7 8 9]"""
arr7 = np.arange(5, 16, 2)
""" Output will be [ 5  7  9 11 13 15] """
print(arr7)

arr8 = np.linspace(10, 20, 10)
"""output will be linerly spaced means distance between two will bw same in all
[10.         11.11111111 12.22222222 13.33333333 14.44444444 15.55555556
 16.66666667 17.77777778 18.88888889 20.   ])"""
print(arr8)

arr9 = arr7.copy()
print(arr9)

#########important Attributes of Numpy##############
print(arr1.shape)
"""Output will be (6,)"""
print(arr2.shape)
""" output will be (2, 3)"""

arr9 = np.array([[1, 2], [5, 7], [5, 4]])


# 3D array
arr10 = np.array([[[1, 2],
                   [3, 4]],
                   
                  [[5, 6],
                   [7, 8]]])
print(arr10.shape)

## ndim : This will give how many dimentional matrix it is
print(arr10.ndim)
print(arr5.ndim)

print(arr1.size) # gives no of items
print(arr1.itemsize) #gives size of each item

## dtype : gives datatype
print(arr9.dtype)

# astype
print(arr10.astype('float'))
      
