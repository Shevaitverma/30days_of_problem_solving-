def binary(arr, k):
    # create a left and right pointers 
    l,h = 0,len(arr)-1
    ans = -1
    while l <= h:
        mid = (l+h)//2
        if k == arr[mid]:
            ans = mid
            h = mid-1
        elif k > arr[mid]:
            l = mid+1
        else:
            h = mid-1
    return ans

arr = [2,3,5,6,8,11,11,14,16,16,16,16,16,16,18]
res = binary(arr, 16)
print(res)