""" Given string ='abcdef' and Pattern is =anything ,ex. 'uurruu' ,Go through
 pattern and if pattern condition is 'u' then Undo(delete letter) from string
 and if condtion is 'r' then REDO it means add back to string  """


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def traverse(self):
        if self.is_empty():
            return "Stack is empty."
        else:
            curr = self.top
            string = ""
            while curr:
                string = string + str(curr.data)
                curr = curr.next
        print(string)

    def pop(self):
        if self.top is None:
            return "Stack is Empty."
        popped_value = self.top

        self.top = self.top.next
        return popped_value.data


def text_editor(text, pattern):

    u = Stack()  # stack for orignal string
    r = Stack()  # Stack to  store undo items
    
    for char in text: # Push whole string in the stack
        u.push(char)

    for command in pattern:  # 'u' is  undo and 'r' Is 'REDO'
        if command == "u":
            if not u.is_empty():
                popped_data = u.pop()
                r.push(popped_data)
        elif command == "r":
            if not r.is_empty():
                popped_data = r.pop()
                u.push(popped_data)

    result = ""

    while (not u.is_empty()):
        result = u.pop() + result # Will give result in top to bottom letters
    print(result)


text_editor("kolkata", "uruur")
