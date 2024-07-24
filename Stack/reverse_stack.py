"""Reverse the given string using stack"""


class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def add_values(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top   
            self.top = new_node

    def traverse(self):
        if self.top == None:
            return "Empty stack"
        else:
            curr = self.top
            while curr:
                print(curr.data)       
                curr = curr.next 

    def pop(self):
        
        popped_value = self.top
        self.top = self.top.next
        return popped_value


def reverse_string(string):
    s = Stack()
    for i  in range(len(string)):
        print(string[i])
        s.add_values(string[i])

    reverse_string = ''
    while s.top:
        popped_value = s.pop()
        reverse_string += popped_value.data
    print(reverse_string)


reverse_string("Hello")
""" Time complaxity will be O(n) as we are using two loops but seprately not
    nested loop.
    And Space complaxity will be O(n) ,as we are increasing size of string ,
    Stack size will be increasing ,so Using Stack for reversing String is not
    good option"""
