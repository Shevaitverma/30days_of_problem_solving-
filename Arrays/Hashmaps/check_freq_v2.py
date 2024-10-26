# ######################################################
# slightly imporved version using hash maps 
#
#  Note: using pre compute array only compute 
#  till 10^6 within scope and 10^7 when declared 
#  globally 
#
# ######################################################

def freq(arr, k):
    max_ele = max(arr)
    # print(max_ele)
    # precompute the hash
    hash_map = [0]*(max_ele+1)
    print(len(hash_map))
    for i in range(len(arr)):
        hash_map[arr[i]] += 1
    print(hash_map)
    # # to check the freq of K 
    return hash_map[k]


arr = [1,2,3,4,4,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,8,9,9,9,9,9,9,14,45,76,100]
# arr = [1,2,3,3,4,5,6,7,7,8]

result = freq(arr, 76)

print(result)