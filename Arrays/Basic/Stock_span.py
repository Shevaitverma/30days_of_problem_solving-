####### brute force approach ###################
#### optimised by stack ######



def solve(arr):
    ans = []
    n = len(arr)

    for i in range(n):
        # print(arr[i])
        count = 0
        for j in range(i, -1, -1):
            if arr[j] <= arr[i]:
                # print(arr[i], arr[j])
                count += 1
            else:
                break
        ans.append(count)
    print(ans)


arr = [100, 80, 60, 70, 60, 75, 85]
# arr = [100, 20, 70, 30, 40, 80 ]
res = solve(arr)

# print(res)