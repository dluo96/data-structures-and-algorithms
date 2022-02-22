class Stack:
    def __init__(self):
        self.items = [] # Implement a stack via a list

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() # pop() is an built-in method for Python lists

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(f"Stack before adding any elements: {s}")
    print(f"Stack is empty: {s.is_empty()}")
    s.push(3)
    print(f"Stack after adding an element: {s}")
    s.push(7)
    s.push(5)
    print(f"Stack after adding another two elements: {s}")
    print(f"Pop the stack: this removes the element {s.pop()}")
    print(f"Stack after pop: {s}")
    print(f"Next element of stack to be popped: {s.peek()}")
    print(f"Final size of stack: {s.size()}")

    # String reversal using a stack
    print("-------------------------------------")
    print("String reversal using a stack")
    string = "!looc era skcatS"
    print(f"Original string: {string}")
    reversed_string = ""
    stack = Stack()

    for char in string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()

    print(f"Reversed string: {reversed_string}")