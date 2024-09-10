def first_repeat(arr):
    hash_map = {}
    
    min_index_of_repeat = float('inf')  ## store maximum and when something is lesser than this then update to minimum value
    first = -1 

    for index, val in enumerate(arr):
        if val not in hash_map:
            hash_map[val] = index
            print("if condition ",hash_map, first, min_index_of_repeat)
        else:
            if hash_map[val] < min_index_of_repeat:
                min_index_of_repeat = hash_map[val]
                # print("hashmap of value ", hash_map[val], val)
                first = val
                print("else condition ", hash_map, first, min_index_of_repeat)
    if first != -1:
        return first
    else:
        return -1
    


arr = [1,2,3,4,5,6,5,5,4,4,3,3,6,5,7]
res = first_repeat(arr)
print(res)