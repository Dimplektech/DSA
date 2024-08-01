def merge_sorted(arr1, arr2, arr):
    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):  # To append left over nums of array
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):  # To append left over nums of array
        arr[k] = arr2[j]
        j += 1
        k += 1

    return


def merge_sort(arr):

    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted(left, right, arr)


arr = [9, 3, 7, 2, 7, 3, 5, 8, 2, 1, 4]
merge_sort(arr)
print(arr)
