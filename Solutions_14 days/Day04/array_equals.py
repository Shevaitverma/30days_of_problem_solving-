
# def check_array(a,b):
#     # checking if array;s length is equal
#     if len(a) != len(b):
#         return "not equal"
#     # sort arrays
#     a.sort()
#     b.sort()
#     dup_array = []
#     for i in range(len(a)):
#         # checking is element of arrays are equal
#         if a[i] == b[i]:
#             dup_array.append(a[i])
#             # testing
#             if debug == True:
#                 print(dup_array)
#         else:
#             return "not equal"
#     return dup_array
debug = False

def check_array(a,b):
    a.sort()
    b.sort()
    if debug == True:
        print("sorted array = ", a," and ",b)
    same_ele = []

    if len(a) <= len(b):
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    if debug == True:
                        print("arary a and b are = ", a[i], " and ", b[j])
                    same_ele.append(a[i])
    else:
        for i in range(len(b)):
            for j in range(len(a)):
                if debug == True:
                    print("array b and a = ",b[i], a[j])
                if b[i] == a[j]:
                    same_ele.append(b[i])
                    

    return same_ele
    

# a = [1,3,2]
# b = [2,4,5,3,1]

# print(check_array(a,b))

def main():
    a1 = [5,7,6,3]
    b1 = [3,12,9,153,167]

    a2 = [93, 0, 1, 2]
    b2 = [0, 93, 5, 7, 9, 12, 15]

    a3 = [10, 2, 50, 100, 200]
    b3 = [1, 3, 5, 9, 12, 15, 17]

    a4 = [1, 2]
    b4 = [5, 9, 3, 4]

    a5 = [1, 2, 7]
    b5 = [1, 3, 4, 5, 7, 6]

    a6 = [9, 3, 2, 6, 14]
    b6 = [1,2]

    a7 = [1, 2, 3, 5]
    b7 = [1, 2, 3, 5]


    print("for array elements: ", a1, "and", b1, "\n",check_array(a1,b1))
    print("for array elements: ", a2, "and", b2, "\n",check_array(a2,b2))
    print("for array elements: ", a3, "and", b3, "\n",check_array(a3,b3))
    print("for array elements: ", a4, "and", b4, "\n",check_array(a4,b4))
    print("for array elements: ", a5, "and", b5, "\n",check_array(a5,b5))
    print("for array elements: ", a6, "and", b6, "\n",check_array(a6,b6))
    print("for array elements: ", a7, "and", b7, "\n",check_array(a7,b7))

if __name__ == "__main__":
    main()