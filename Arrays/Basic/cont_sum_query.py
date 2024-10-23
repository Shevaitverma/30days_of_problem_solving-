#####  brute force approach 

# def solve(a, b):
#     # created array with A zeros
#     arr = [0]*a 
#     for query in b:
#         s = query[0]-1
#         e = query[1]-1
#         val = query[2]
#         for i in range(s, e+1):
#             arr[i] += val
#     return arr

# # a = 5 # number of rows
# # b = [[1,2,10],[2,3,20],[2,5,25]]
# a = 1000
# b = [[101, 145, 12],[425, 856, 10],[771, 499, 15],[951, 978, 13],[666, 789, -45],[130, 890, 41], [266, 999, -15],[331, 778, 13], [441, 999, 15],[651, 898, 73], [1, 39, 15],[51, 100, -33]]



# res = solve(a, b)
# print(res)

####### slight optimization 
def solve(a, b):
    # created array with A zeros
    arr = [0]*a 
    for query in b:
        s = query[0]-1
        e = query[1]-1
        val = query[2]
        arr[s] += val
        if e+1 < len(arr):
            arr[e+1] -= val
    for i in range(1, a):
        arr[i] += arr[i-1]

    return arr

# a = 5 # number of rows
# b = [[1,2,10],[2,3,20],[2,5,25]]
a = 100
b = [[10, 45, 12],[5, 56, 10],[1, 99, 15],[51, 78, 13],[66, 89, -45],[30, 90, 41], [66, 99, -15],[31, 78, 13], [1, 99, 15],[51, 98, 73], [1, 39, 15],[51, 100, -33]]


res = solve(a, b)
print(res)