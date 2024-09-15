def q_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        q_sort(arr, low, pivot - 1)
        q_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  
    i = low + 1
    j = high

    while True:
        # Find the first element less than or equal to pivot
        while i <= j and arr[i] <= pivot:
            i += 1
        # Find the first element greater than pivot
        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]  # Swap the pivot element with arr[j]
    return j  # Return the pivot index

def quick(arr):
    q_sort(arr, 0, len(arr) - 1) 
    return arr  

arr = [4, 6, 5, 3, 7, 8, 1, 9, 2]
res = quick(arr)

print(res)
