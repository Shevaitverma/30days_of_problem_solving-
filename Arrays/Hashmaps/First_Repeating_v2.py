def first_repeat(arr):
    # create freq map 
    freq_map = {}
    for ele in arr:
        if ele in freq_map:
            freq_map[ele] += 1
        else:
            freq_map[ele] = 1
    
    # check if ele is greater than 1
    for ele in arr:
        if freq_map[ele] > 1:
            return ele
    return -1
    


arr = [1,2,3,4,5,6,5,5,4,4,3,3,6,5,7]
res = first_repeat(arr)
print(res)