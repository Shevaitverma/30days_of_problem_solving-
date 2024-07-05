# array revers using two pointers
def reverse(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print("Original: ", arr)
reversed_arr = reverse(arr)
print(f"New_array: {reversed_arr}")