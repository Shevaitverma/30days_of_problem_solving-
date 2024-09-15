# find fibonacci number in series
def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacchi(n-1)+fibonacchi(n-2)


num = 10
print(fibonacchi(num))

