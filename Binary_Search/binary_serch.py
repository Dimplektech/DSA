""" Recursive Binary search"""


def binary_search(arr, low, high, item):
    if low <= high:
        mid = (low + high)//2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
            return binary_search(arr, low, high, item)
        else:
            low = mid + 1
            return binary_search(arr, low, high, item)    
    else:
        return -1    


arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]    
high = len(arr) - 1
index = binary_search(arr, 0, high, 11)
print(index)