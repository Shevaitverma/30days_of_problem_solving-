##### information 
'''
we have: 
    K = given
    Arr = given     
    find sub arrays whose sum are evenly divisible by k 

    1. (sum of sub-arrays) % k == 0
'''


Debug = False
# check if sum of sub arrays is evenly divisible by k or nor 

def solve(arr, k):
    #find all sub arrays 
    sub_arrays = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if Debug == True:
                print(f"all sub arrays of {arr[i]} and {arr[j]} are {arr[i:j+1]}")
            sub_arrays.append(arr[i:j+1])
    
    # find sum of sub-arrays which are evenly divisible by k
    k_sub_arrays = []
    not_included = []
    for i in range(len(sub_arrays)):
        if sum(sub_arrays[i])%k == 0:
            if Debug == True:
                print("needed sub array",sub_arrays[i])
            k_sub_arrays.append(sub_arrays[i])
        else:
            not_included.append(sub_arrays[i])

    return k_sub_arrays, not_included


# test 
arr = [1,2,3,4,12,14,22]
k = 3


k_sub_arr, not_k_sub_arr= solve(arr, k)
print("sub arrays which are divisible by k are : ", k_sub_arr)
print("not included sub arrays are; ", not_k_sub_arr)