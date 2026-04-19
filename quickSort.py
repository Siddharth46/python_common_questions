# quick sort implementation
arr = [2,6,5,0,3,8,12,1]

def partition(arr, low, high):
    x = arr[low]
    i = low
    for j in range(low, high+1):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    return i

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, pi+1, high)
        quickSort(arr, low, pi-1)


n = len(arr) -1
quickSort(arr, 0, n)

print(arr)

