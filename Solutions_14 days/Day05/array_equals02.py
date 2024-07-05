########    slightly imporave version  #########
debug = True
def check_array(a,b):
    a.sort()
    b.sort()
    if debug == True:
        print("sorted array = ", a," and ",b)
    same_ele = []

    if len(a) > len(b):
        b,a = a,b

    for i in range(len(a)):
        for j in range(len(b)):
            if debug == True:
                print("arary a and b are = ", a[i], " and ", b[j])
            if a[i] == b[j]:
                same_ele.append(a[i])
            elif (a[i] < b[j]):
                b = b[j:(len(b)+1)]
                if debug == True:
                    print("The revised array is",b)
                break

    
                    

    return same_ele
    



### main function ###
def main():
    ######  test arrays ######
    a1, b1 = [5,7,6,3],[3,12,9,153,167]
    a2,b2 = [93, 0, 1, 2],[0, 93, 5, 7, 9, 12, 15]
    a3,b3 = [10, 2, 50, 100, 200],[1, 3, 5, 9, 12, 15, 17]
    a4, b4 = [1, 2],[5, 9, 3, 4]
    a5, b5 = [1, 2, 7],[1, 3, 4, 5, 7, 6]
    a6, b6 = [9, 3, 2, 6, 14],[1,2]
    a7, b7 = [1, 2, 3, 5],[1, 2, 3, 5]


    print("for array elements: ", a1, "and", b1, "\nDuplicates = ",check_array(a1,b1))
    print("for array elements: ", a2, "and", b2, "\nDuplicates = ",check_array(a2,b2))
    print("for array elements: ", a3, "and", b3, "\nDuplicates = ",check_array(a3,b3))
    print("for array elements: ", a4, "and", b4, "\nDuplicates = ",check_array(a4,b4))
    print("for array elements: ", a5, "and", b5, "\nDuplicates = ",check_array(a5,b5))
    print("for array elements: ", a6, "and", b6, "\nDuplicates = ",check_array(a6,b6))
    print("for array elements: ", a7, "and", b7, "\nDuplicates = ",check_array(a7,b7))

if __name__ == "__main__":
    main()