def dec_inc(n):
    if n == 0:
        return 
    print(n, end=" ")
    dec_inc(n-1)
    print(n, end=" ")


n = 5
dec_inc(n)