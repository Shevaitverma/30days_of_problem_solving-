def solve(arr):
    unique = []
    i = 1
    while i < len(arr):
        if arr[i-1] == arr[i]:
            i += 1
        else:
            unique.append(arr[i-1])
            i += 1
    unique.append(arr[-1])

    #     if i not in unique:
    #         unique.append(i)
    return unique

arr = [1,2,3,3,4,4,5,5,5,5,6]

res = solve(arr)
print(res)