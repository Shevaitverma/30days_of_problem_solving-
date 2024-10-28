from stack_util import Stack

def solve(arr):
    n = len(arr)
    ans = []
    stack = Stack()  # Use the custom Stack class

    for i in range(n):
        # Pop elements from the stack while they are less than or equal to arr[i]
        while not stack.is_empty() and arr[stack.top()] <= arr[i]:
            stack.pop()

        # Determine the span
        if stack.is_empty():
            span = i + 1
        else:
            span = i - stack.top()

        # Append the span to the result list
        ans.append(span)

        # Push the current index onto the stack
        stack.push(i)

    return ans



arr = [100, 80, 60, 70, 60, 75, 85]
res = solve(arr)
print(res)
