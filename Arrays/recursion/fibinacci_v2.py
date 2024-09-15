# create fibonacci series till numner 
def fibonacchi(n):
    fib = []
    fib.append(0)
    fib.append(1)
    fib.append(1)

    i=3
    while i<=n:
        fib.append(fib[i-1] + fib[i-2])
        i+=1

    #            or
    #     
    # for i in range(3, n+1):
    #     fib.append(fib[i-1] + fib[i-2])

    return fib

num = 10
print(fibonacchi(num))

