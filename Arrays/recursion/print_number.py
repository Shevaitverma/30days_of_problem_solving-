# print numbers from 1 to n 

def print_number(n):
    if n == 0:
        return
    print_number(n-1)
    print(n, end=" ")

num = 10
print_number(num)