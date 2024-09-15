def print_arr(arr):
    if len(arr) == 0:
        return
    print(arr[0], end=" ")
    print_arr(arr[1:])
    


arr = [1,2,3,4,5]
print_arr(arr)
