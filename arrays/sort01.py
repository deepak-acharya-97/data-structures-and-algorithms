def sort01(arr):
    low = 0
    high = len(arr)-1
    while(low <= high):
        if(arr[low] == 1):
            arr[low], arr[high] = arr[high], arr[low]
            high -= 1
        else:
            low += 1

def sort01_ver1(arr):
    low = -1
    high = len(arr)-1
    for ind, val in enumerate(arr):
        if(val == 0):
            low += 1
            arr[low], arr[ind] = arr[ind], arr[low]

arr = [0, 1, 0, 1, 0, 1, 0, 0, 0]
sort01_ver1(arr)
print(arr)