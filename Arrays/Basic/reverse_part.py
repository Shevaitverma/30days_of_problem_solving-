# reverse part of an arary

def reverse2(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print("Original: ", arr)
reversed_arr = reverse2(arr,1,3)
print(f"New_array: {reversed_arr}")