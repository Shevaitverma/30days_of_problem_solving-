def binary(arr, k):
    # create a left and right pointers 
    l,h = 0,len(arr)-1

    while l <= h:
        mid = (l+h)//2
        if k == arr[mid]:
            return mid
        elif k > arr[mid]:
            l = mid+1
        else:
            h = mid-1
    return "index not found"

arr = [2,3,5,6,8,11,14,16,18]
res = binary(arr, 16)
print(res)