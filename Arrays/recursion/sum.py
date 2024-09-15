def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

n = 4
res = sum(n)
print(res)