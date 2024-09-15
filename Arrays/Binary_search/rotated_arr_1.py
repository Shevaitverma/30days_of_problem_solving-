def rotated(arr,k):
    l = 0 
    h = len(arr) - 1

    while l <= h:
        mid = (l+h)//2

        if arr[mid] == k:
            return mid
        
        # check if left side is sorted
        if arr[l] <= arr[mid]:
            # check if k is in left side
            if arr[l]<=k and k<=arr[mid]:
                h=mid-1
            # k is in right side
            else:
                l=mid+1
        # right side is sorted
        else:
            # check if k is in right side
            if arr[mid]<=k and k<=arr[h]:
                l=mid+1
            # k is in left side
            else:
                h=mid-1

        

arr = [7,8,9,1,2,3,4,5,6]
res = rotated(arr,8)
print(res)