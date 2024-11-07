from stack_util import Stack

def solve(s):
    # created stack
    stack = Stack()

    # iterate over each char
    for char in s:
        # if opening -> push to stack 
        if char in "({[":
            stack.push(char)
        elif char in ")}]": # if closing 
            # check if stack is empty 
            if not stack:
                return False
            top = stack.pop()
            # Directly compoare the char
            if char == ")" and top != "(":
                return False
            elif char == "}" and top != "{":
                return False
            elif char == "]" and top != "[":
                return False
    # if stack is empty, means it's balanced 
    return stack.size() == 0

# Test cases
print(solve("()"))  # True
print(solve("()[]{}"))  # True
print(solve("(]"))  # False
print(solve("([)]"))  # False
print(solve("{[]}"))  # True