a = [5,6,9,12]
b = [10,15,25,32,34,72.1342,2234,2347]

for i in range(0,len(a)-1):
    n1, n2 = a[i], a[i+1]
    subset = []
    for j in range(len(b)):
        if((n1*n2)<b[j]):
            for k in range(i, len(b)):
                subset.append(b[k])
            print(f"({n1},{n2}) = {b}")
            break
        else:
            print(f"({n1},{n2}) = {subset}")
            break
#b = b[j:(len(b)+1)]