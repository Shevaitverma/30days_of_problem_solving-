from stack_util import Stack

def solve(s):
    # created stack
    stack = Stack()

    # dict to match 
    matching_para = {
        ')': '(', 
        '}': '{', 
        ']': '['
    }

    # iterate over each char
    for char in s:
        # if opening -> push to stack 
        if char in "({[":
            stack.push(char)
        elif char in ")}]": # if closing 
            # check if stack is empty 
            if not stack or stack.top() != matching_para[char]:
                return False
            stack.pop() # pop this matching opening parenthesis
    
    # if stack is empty, then parenthesis are balanced 
    if stack.size() == 0:
        return True
    else:
        return False

# Test cases
print(solve("()"))  # True
print(solve("()[]{}"))  # True
print(solve("(]"))  # False
print(solve("([)]"))  # False
print(solve("{[]}"))  # True