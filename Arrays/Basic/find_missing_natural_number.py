#### we have an array in which we need to find first missing number, ans should be +ve int...
## eg:  [3, -1, 1, 2, 7] , ans = 4 
##  [9 2 6 4 -8 1 3], ans = 5 
##  [1 0 -5 -6 4 2], ans = 3



############ bruteforce approach #############
### loop over the whole sorted array and check if the number is missing if yes then increase the missing number
###   but checking should be inside another check that is if number is positive or not

# def find_missing(arr):
#     missing_number = 1
#     arr.sort()

#     for num in arr:
#         if num > 0:
#             if num == missing_number:
#                 missing_number += 1
#     return missing_number




############   optimial solution #################

def find_missing(arr):
    n=len(arr)

    # replace all with -ve numbers with N+2
    for i in range(n):
        if arr[i] <= 0:
            arr[i] = n+2

    # mark all ele at index as -ve: 
    for i in range(n):
        ele = abs(arr[i])
        index = ele - 1
        if index < n:
            arr[index] = -1 * abs(arr[index])
     
    # return the answer
    for i in range(n):
        if arr[i] > 0:
            return i+1
    return n+1


arr = [3, -1, 1, 2, 7] 

res = find_missing(arr)
print(res)