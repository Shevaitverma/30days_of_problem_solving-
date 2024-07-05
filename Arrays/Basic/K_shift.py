# perforn the shifting K times

def k_shift(arr, k):
  # store last ele
  for i in range(k):
    # last = arr.pop()
    last = arr[-1]
    for j in range(len(arr)-2, -1, -1):
      arr[j+1] = arr[j]
    arr[0] = last
  return arr

arr = [1, 2, 3, 4, 5]
print("original: ", arr)
k_shifted_arr = k_shift(arr, 2)
print(f"new array: {k_shifted_arr}")