# Creating your own dynamic list
import ctypes


class MyList:
    def __init__(self):
        self.size = 1  # Size of the array
        self.n = 0  # how many items are there in the list.
        # Create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        self.n

    def __str__(self) -> str:
        # [1,2,3]
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ","

        return "[ " + result[:-1] + " ]"  # slice Last comma of the string.


    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return "IndexError-Index out of range."

    def append(self, item):
        if self.n == self.size:
            #  Resize an array size
            self.__resize(
                self.size * 2
            )  # Create the array of double the size of prev arra
        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return "Empty List"
        
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1 

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i

        return 'ValueError - not in the List'    

    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1): # Reverse loop.
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def __delitem__(self, pos):
        for i in range(pos, self.n-1):
            self.A[i] = self.A[i+1]

        self.n = self.n - 1   

    def __resize(self, new_capacity):
        # Create a new array with new capacity.
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # Copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __make_array(self, capacity):
        # Creates a Ctype array (static,referential) with the Size capacity
        return (capacity * ctypes.py_object)()


L = MyList()
L.append("Hello")
L.append(3.4)
L.append(True)
L.append(100)
print(L)
print(L[3])
L.pop()
print(L)
# L.pop()
# print(L)
# L.pop()
# print(L)
# L.pop()
# print(L)
L.clear()
print(L)
L.append("Hello")
L.append(3.4)
L.append(True)
L.append(100)
print(L.find(3.4))
print(L.find(True))
print(L.find(1000))
L.insert(1,'Apple')
L.insert(0,0)
print(L)
del L[2]
print(L)


