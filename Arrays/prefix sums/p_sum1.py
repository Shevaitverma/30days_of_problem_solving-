# find array prefix sum 
def p_sum(arr):
  n = len(arr)
  pf = [0] * n
  for i in range(0,n):
    sum = 0
    for j in range(0, i+1):
      sum += arr[j]
    # print(f"sum of {i} = {sum}")
    pf[i] = sum
  return pf

arr = [10, 32, 6, 12, 20, 1]
print(p_sum(arr))