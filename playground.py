def first_repeat(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(i+1, n+1):
            if arr[i] == arr[j]:
                return arr[i]

arr = [1,2,3,4,5,6,5,5,4,4,6,5,7]
res = first_repeat(arr)
print(res)