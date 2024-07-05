# find array prefix sum - optimisation  
def p_sum(arr):
  n = len(arr)
  pf = [0] * n
  pf[0] = arr[0]
  for i in range(1, n):
    pf[i] = pf[i-1] + arr[i]
  return pf

arr = [10, 32, 6, 12, 20, 1]
print(p_sum(arr))