# check unique element using hashset

########### brute force ##
# def solve(arr):
#     unique = []
#     i = 1
#     while i < len(arr):
#         if arr[i-1] == arr[i]:
#             i += 1
#         else:
#             unique.append(arr[i-1])
#             i += 1
#     unique.append(arr[-1])

#     #     if i not in unique:
#     #         unique.append(i)
#     return unique

########## optimised  #####
def unique(arr):
    unique_ele = set(arr)
    return unique_ele 


arr = [3,4,3,5,6,6,7,3,2,4,5,6,3,2,3,4]
res = unique(arr)

print(res)