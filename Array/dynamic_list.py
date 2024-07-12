# To check how Python List works as Dynamic array
import sys
L= []
print(sys.getsizeof(L))
L.append('hello')
print(sys.getsizeof(L))
L.append('World')
print(sys.getsizeof(L))
L.append(1)
print(sys.getsizeof(L))
L.append(2)
print(sys.getsizeof(L))
L.append(3)
print(sys.getsizeof(L))
L.append(4)
print(sys.getsizeof(L))
print(L)

# Example  2: Observe how Python List works as dynamic array
L = []

for i in range(100):
    print(i, sys.getsizeof(L))
    L.append(i)
