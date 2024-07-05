def alpha(a, b):

    # Find common elements
    common = []
    for i in a:
        for j in b:
            if i == j:
                common.append(i)

    # Combine both lists
    existing_list = a + b
    full_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Find remaining elements
    remaining_list = []
    for ele in full_list:
        if ele not in existing_list:
            remaining_list.append(ele)

    print("Common elements are =", common)
    print("Remaining elements =", remaining_list)



def main():
    a,b = ["a", "b", "c"],["d", "c", "f", "g"]
    a1,b1 = ["a", "b", "c", "j", "r"],["d", "c", "f", "b", "a", "g", "k", "l"]
    a2,b2 = ["y", "u", "t"],["t", "c", "f", "h", "y", "z","k"]

    alpha(a,b)
    print()
    alpha(a1,b1)
    print()
    alpha(a2,b2)


if __name__ == "__main__":
    main()