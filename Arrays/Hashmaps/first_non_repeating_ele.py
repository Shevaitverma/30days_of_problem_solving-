def non_rep(arr):
    # create a freq hashmap
    freq_map = {}

    for ele in arr:
        if ele not in freq_map: 
            freq_map[ele] = 1
        else: 
            freq_map[ele] += 1

    # return non repeating element by simply check for value == 1 in hashmap
    for ele in arr:
        if freq_map[ele] == 1:
            return ele
    return -1




arr = [1,2,3,4,5,6,8,1,5,5,4,4,3,3,6,5,7]

res = non_rep(arr)
print(res)