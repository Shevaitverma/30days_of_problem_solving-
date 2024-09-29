import time

def min_operations(n,k):
    operation_count = 0
    
    while n > 0:
        if k == 1:
            # If k is 1, we can only subtract 1 each time
            return operation_count + n
            
        curr_power=1
        while curr_power <= n:
            curr_power *= k
        # Move back to the last valid power
        curr_power //= k
        # print("curr of each iteration ",curr_power)
    
        n -= curr_power
        # print("value after iteration ",n)
        operation_count += 1
    
    return operation_count

n,k = 9999999999999999, 1111111
start_time = time.time()
res = min_operations(n,k)
print(res)
print("--- %s seconds ---" % (time.time() - start_time))
# t = int(input())

# for _ in range(t):
#     n, k = map(int, input().split())
#     res = min_operations(n,k)
#     print(res)


