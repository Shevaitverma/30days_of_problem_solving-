def merge(arr1, arr2): 
    m = len(arr1)
    n = len(arr2)
    ans = []

    i = 0
    j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < m:
        ans.append(arr1[i])
        i += 1

    while j < n:
        ans.append(arr2[j])
        j += 1

    return ans




a = [2,4,7,8,12,13,15,17]
b = [3,5,6,7,9,12,14,15,18]

res = merge(a,b)

print(res)