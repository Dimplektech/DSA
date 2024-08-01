def selection_sort(arr):
  
    for i in range(len(arr)-1):
        print(i+1, "pass", end=" ") # To just show which pass it is
        min = i
        print("current min is", arr[min])
        for j in range(i+1, len(arr)):
            print("current number under observation",arr[j])
            if arr[j] < arr[min]:
                print("current value is less than min",arr[min])
                min = j
                print("Now min has become ",arr[min])

        arr[i], arr[min] = arr[min], arr[i]
        print("*"*20)
    print(arr)


arr = [34, 12, 5, 76, 23, 89, 17, 87, 99, 23, 45]        
selection_sort(arr)
