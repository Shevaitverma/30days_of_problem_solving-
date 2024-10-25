# note: 2D array must be sorted both rows and column wise 

###### bruteforce approach 

########################################################################
#                                                                      #
#  iterating the whole 2D array and check if it's euqal to the target  #
#                                                                      #
########################################################################

####### optimised approach

def solve(a, b):
    n=len(a)
    m=len(a[0])
    i=0
    j=m-1
    while i<n and j>=0:
        if a[i][j] == b:
            return print(f"target present at row {i+1} and col {j+1}")

        elif a[i][j] > b:
            j-=1
        else:
            i+=1
    return print("target not present")

arr = [
    [-5, -2, 1, 13],
    [-4, 5, 3, 14],
    [-3, 2, 5, 18],
    [2, 6, 10, 20]
]
target = 5
res = solve(arr, target)
# print(res)