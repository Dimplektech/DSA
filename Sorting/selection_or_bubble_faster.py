import random
import time
L = []
for i in range(10000):
    L.append(random.randint(1, 10000))

L1 = L[:]  # copy L to L1, now both list has Same data
""" now check with bubble sort and Selection sort , 
which sort takes more time to sort same Lists"""    

def bubble_sort(arr):
    for i in range(len(arr)-1):  # Going through each pass
        for j in range(len(arr)-1-i):  # No of comparisions, every pass
            # comparison will be less, as last  i items will be sorted.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def selection_sort(arr):
  
    for i in range(len(arr)-1):
      #  print(i+1, "pass", end=" ") # To just show which pass it is
        min = i
      #  print("current min is", arr[min])
        for j in range(i+1, len(arr)):
          #  print("current number under observation",arr[j])
            if arr[j] < arr[min]:
          #      print("current value is less than min",arr[min])
                min = j
           #     print("Now min has become ",arr[min])

        arr[i], arr[min] = arr[min], arr[i]
       # print("*"*20)
    return arr


start = time.time()
bubble_sort(L)
print("Time Taken for bubble sort", time.time() - start, "secs")

start = time.time()
selection_sort(L1)
print("Time Taken for slection sort", time.time() - start, "secs")



