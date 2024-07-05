def sum1(arr, l, r):
  sum = 0
  for i in range(l, r+1):
    sum += arr[i]
    # print(f"sum at {i} = ", sum)
  return sum

arr = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
l = 4
r = 8
print(sum1(arr, l, r))