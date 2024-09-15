# Implement pow(A, B) % C.
def solve(A, B, C):
        if(A == 0):
            return 0
        if(B == 0):
            return 1
        ans = solve(A, B // 2 , C)
        ans = (ans * ans) % C
        if(B % 2 == 1):
            ans = (ans * A) % C
        return ans


A = 2
B = 3
C = 3

res = solve(A,B,C)
print(res)