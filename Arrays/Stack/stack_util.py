class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. No item to pop.")
            return None

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def size(self):
        return len(self.stack)
