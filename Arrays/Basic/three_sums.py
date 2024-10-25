#####   3 sums:  in an array find all subarrays of three, whose sum is 0

def solve(arr):
    n = len(arr)
    result = []

    def two_sum(arr, target, i, j):
        while i < j:
            if arr[i] + arr[j] > target:
                j -= 1
            elif arr[i] + arr[j] < target:
                i += 1
            else:
                # Found a triplet
                result.append([-target, arr[i], arr[j]])
                
                # Move to the next different element
                while i < j and arr[i] == arr[i + 1]:
                    i += 1
                while i < j and arr[j] == arr[j - 1]:
                    j -= 1
                
                i += 1
                j -= 1

    if n < 3:
        return []

    # Sort the array
    arr.sort()

    # Fix one element
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue  # Skip duplicates

        # Set the target for two_sum
        n1 = arr[i]
        target = -n1

        two_sum(arr, target, i + 1, n - 1)

    return result

arr = [-1, 0, 1, 2, -1, -4]
res = solve(arr)
print(res)
