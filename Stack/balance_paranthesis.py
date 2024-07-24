"""Using Stack :  Check Expression whether it is balanced paranthesis. """


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, value):
        new_data = Node(value)
        new_data.next = self.top
        self.top = new_data

    def traverse(self):
        curr = self.top
        while curr != None:
            print(curr.data)
            curr = curr.next

    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        else:
            return self.top.data

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            popped_value = self.top
            self.top = self.top.next
            return popped_value

    def size(self):
        count = 0
        if self.top == None:
            return 0
        else:
            curr = self.top
            while curr:
                count += 1
                curr = curr.next
        return count


def is_balanced(expression):

    s = Stack()

    matching_paren = {")": "(", "}": "{", "]": "["}

    for char in expr:
        if char in matching_paren.values():  # If it's an opening bracket.
            s.push(char)
        elif char in matching_paren.keys():  # If it's a closing bracket.
            if s.is_empty() or s.peek() != matching_paren[char]:
                return False  # Not balanced
            s.pop()
    return s.is_empty()  # If stack is empty, then it's balanced.


expr = "[(a+b)+(c+d)]"
if is_balanced(expr):
    print("Expression is balanced")
else:
    print("Expression is not balanced")
