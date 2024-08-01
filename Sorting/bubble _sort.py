def bubble_sort(arr):
    for i in range(len(arr)-1):  # Going through each pass
        for j in range(len(arr)-1-i):  # No of comparisions, every pass
            # comparison will be less, as last  i items will be sorted.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


arr = [34, 17, 98, 56, 32, 90, 67, 78]
bubble_sort(arr)
