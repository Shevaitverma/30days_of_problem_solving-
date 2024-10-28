from stack_util import Stack

# Create a Stack object
my_stack = Stack()

# Test stack operations
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack.stack)

print("Top item:", my_stack.top())   
print("Stack size:", my_stack.size())

print("Popped item:", my_stack.pop())
print("Stack size after pop:", my_stack.size()) 

print("Is stack empty?", my_stack.is_empty())
print(my_stack.stack)