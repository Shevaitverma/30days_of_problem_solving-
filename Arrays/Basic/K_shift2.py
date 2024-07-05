# perforn the shifting K times ----- optimization

def k_shift(arr, k):
  # reverse whole array
  arr[:] = arr[::-1]
  # print("step1: ", arr)

  # reverse front part
  arr[0:k] = arr[0:k][::-1]
  # print("step2: ", arr)

  # reverse second part
  arr[k:len(arr)] = arr[k:len(arr)][::-1]
  # print("step3: ", arr)

  return arr

arr = [1,2,3,4,5,6,8,8,7,12,32,42,51,12,23,34]
print("original: ", arr)
k_shifted_arr = k_shift(arr, 5)
print(f"new array: {k_shifted_arr}")