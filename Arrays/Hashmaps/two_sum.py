# two sum problem 


# ##########  brute force approach ##########
# def solve(arr, k):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] + arr[j] == k:
#                 return [i, j]

# def solve(arr, k):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1, n):
#             if(k-arr[i]==arr[j]):
#                 return [i, j]
#             else:
#                 return "sum is not possible"

######### optimal approach ############

####
###    time complexity is O(n)
####
### 
def solve(arr,k):
    n = len(arr)
    # create a hash map 
    hash_map = {}
    for i in range(n):
        if arr[i] in hash_map:
            return [hash_map[arr[i]], i]
        else:
            hash_map[k-arr[i]] = i


arr = [2,7,11,15]
# arr = [1,2,4,7,8,10]
k=9
res = solve(arr, k)
print(res)