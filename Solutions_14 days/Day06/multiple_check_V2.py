def returnsubsetarr (num1, num2, arraytoparse):
    numtocompare = num1 * num2
   # subset = []
    for j in range(len(arraytoparse)):
        if(numtocompare < arraytoparse[j]):
            arraytoparse = arraytoparse[j:(len(arraytoparse))]
            break
    return arraytoparse
        
#b = b[j:(len(b)+1)]


# a = [5,6,9,12]
# b = [10,15,25,32,34,72,1342,2234,2347]

## test arrays 
a,b = [2,4,5,7,8,9,12],[22,25,29,32,36,37,45,86,95,112,233,345,432]
# a,b = [5,6,9,12],[10,15,25,32,34,72,1342,2234,2347]

a.sort()
b.sort()

for i in range(0,len(a)-1):
    print(f"The set for {a[i]}, {a[i+1]} is {returnsubsetarr(a[i], a[i+1],b)}")
    
    
    
    
    