# print numbers from 1 to n 

def print_number(n):
    if n == 1:
        print(n, end=" ")
    else:
        print(n, end=" ")
        print_number(n-1)

num = 10
print_number(num)