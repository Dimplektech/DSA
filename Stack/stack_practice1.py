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


s = Stack()
print(s.is_empty())
s.push(21)
s.push(12)
s.push(34)
s.push(78)
s.traverse()
print("==============")
print(s.peek())
print("==============")
s.pop()
s.traverse()
print("==============")
s.pop()
s.traverse()
print("==============")
s.pop()
s.traverse()
print("==============")
s.pop()
s.traverse()
print("==============")
s.pop()
s.traverse()
