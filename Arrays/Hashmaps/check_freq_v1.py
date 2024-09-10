# checking frequency of given element using bruteforce approcah 
def freq(arr, k):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] == k:
            count += 1
            # print(arr[i], count)
    return count    
    # print(count)

arr = [1,2,3,4,4,5,6,6,6,7,8,9,9,9,9,9,9]

result = freq(arr, 9)

print(result)