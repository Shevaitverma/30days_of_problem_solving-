debug = True

def solve(arr):
    # we only need odd numner of elements in arrry 
    if len(arr) % 2 == 0:
        return "array must be odd !!!!!!!!!!!"

    # array must be in sorted order
    arr.sort()

    # find mid point
    mid = len(arr)//2
    mid_ele = arr[mid]

############### basic approach #################
    # check for larger and smaller subarr
    larger = []
    smaller = []
    for i in range(len(arr)):
        if arr[i] < mid_ele:
            smaller.append(arr[i])
        elif arr[i] > mid_ele:
            larger.append(arr[i])
    if debug == True:
        print(f"larger = {larger}, smaller = {smaller} and mid = {[mid_ele]}")

    # rearrange arrarray
    new_arr = larger[::-1] + [mid_ele] + smaller

    return new_arr

# b = b[j:(len(b)+1)]



def maim():
    arr = [1,2,3,4,5]
    arr2 = [1,2,3,4,5,6,7,8,9]
    arr3 = [4,5,6,7,8,9,10]
    arr4 = [9,11,13,15,18,19,21,24,25,33,35]


    print(solve(arr))
    print(solve(arr2))
    print(solve(arr3))
    print(solve(arr4))

if __name__ == "__main__":
    maim()