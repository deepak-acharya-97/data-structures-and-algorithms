def sort01(arr):
    low = 0
    high = len(arr)-1
    while(low <= high):
        if(arr[low] == 1):
            arr[low], arr[high] = arr[high], arr[low]
            high -= 1
        else:
            low += 1

arr = [0, 1, 0, 1, 0, 1, 0, 0, 0]
sort01(arr)
print(arr)