# two sum 2 --- one based index 
### here array is sorted
####
###    time complexity is slightly less than O(n)
####
###

#############  optimisation ###########`
def solve(arr, k):
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j]==k:
            return [i+1, j+1]
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1


arr = [2,7,11,15]
k=9

res = solve(arr, k)
print(res)