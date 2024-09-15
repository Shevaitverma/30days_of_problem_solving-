def merge_sort(arr):
    
    # function for merge two sorted arrays
    def merge(arr1, arr2): 
        m = len(arr1)
        n = len(arr2)
        ans = []
        i = 0
        j = 0
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        while i < m:
            ans.append(arr1[i])
            i += 1
        while j < n:
            ans.append(arr2[j])
            j += 1
        return ans
    
    # function to split it into two sorted arrays
    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    return sort(arr)
    
    

arr = [4,3,2,6,5,8,6,8,0,7,5,1,2]
res = merge_sort(arr)

print(res)