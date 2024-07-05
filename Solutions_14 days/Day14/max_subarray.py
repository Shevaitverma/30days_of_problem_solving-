'''
we have an array, we need to check the maximum subarray sum.
'''

def max_subarray_sum(arr):
    # convert to float value to avoid overflow warnings when converting to float value from string value
    max_sum = float('-inf') 
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  

arr = [1, 2, 3, 4, 5]
print(max_subarray_sum(arr)) 