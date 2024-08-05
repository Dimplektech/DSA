
############ python List VS numpy Array      ####
import sys
import time
import numpy as np 

lista = range(100)  # python list
arr11 = np.arange(100) # Numpy array

print(sys.getsizeof(87)*len(lista))
# output will be 2800 bytes
print(arr11.itemsize * arr11.size)
# output will be 400 bytes
"""means numpy array takes less spce in memory than python list"""


####numpy array is faster than python list

# Time taken by python array
x = range(10000000)
y = range(10000000, 20000000)

start_time = time.time()

c = [x+y for x, y in zip(x, y)]

print(time.time() - start_time)

# Time taken by Numpy array
a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start_time = time.time()
c = a + b   # easy code
print(time.time() - start_time)
