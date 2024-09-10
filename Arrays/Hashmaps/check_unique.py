# check unique element using hashset

def unique(arr):
    unique_ele = set(arr)
    return unique_ele 


arr = [3,4,3,5,6,6,7,3,2,4,5,6,3,2,3,4]
res = unique(arr)

print(res)