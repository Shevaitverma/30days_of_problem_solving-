def dup(arr):
    seen = []
    duplicates = False
    for i in range(len(arr)-1):
        if arr[i] in seen:
            duplicates = True
        else:
            seen.append(arr[i])
    return duplicates

# tests
a1 = [1,2,3,4,5,6,7,8,9]
a2 = [1,2,23,4,5,11,16,9]
a3 = [1,2,5,4,5,6,7,8,9]
a4 = [11,2,3,4,11,6,7,8,9]

# dup(arr)
print(dup(a1))
print(dup(a2))
print(dup(a3))
print(dup(a4))