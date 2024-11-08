from stack_util import Stack

def solve(s):
    # create a stack 
    stack = Stack()

    for char in s:
        # check if stack is empty 
        if stack.is_empty():
            stack.push(char)
        else:
            if stack.top() == char:
                stack.pop()
            else: 
                stack.push(char)
    result = "".join(stack.stack)
    return result


# Test cases
print(solve("abbd"))  # ad
print(solve("abccbde"))  # ade
print(solve("abbbd"))  # abd
print(solve("abbcbbcacx"))  # cx