class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    
class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node 

    def pop(self):
        if self.top == None:
            return "Empty"
        else:
            popped_data = self.top
            self.top = self.top.next 
        return popped_data.data   

    def traverse(self):
        curr = self.top
        while curr:
            print(curr.data)
            curr = curr.next

    def size(self):
        count = 0
        curr = self.top
        while curr:
            count = count + 1
            curr = curr . next
        return count    


class QueueUsingStack:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enque(self, value):
        self.s1.push(value)

    def dequeue(self):
        
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

        if self.s2.is_empty() and self.s1.is_empty():
            return "empty queue"
        self.s2.pop()        

    def traverse(self):
        # For demonstration, we can print both stacks
        print("Stack 1:")
        self.s1.traverse()
        print("Stack 2:")
        self.s2.traverse()    
        

queue = QueueUsingStack()
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(6)
queue.enque(20)


print("Queue after enqueuing 2,3,4,6,20:")
queue.traverse()
print("**************************")

print("Dequeue Operation : ")
queue.dequeue()
queue.traverse()
print("**************************")

print("Dequeue Operation : ")
queue.dequeue()
queue.traverse()
print("**************************")

print("Dequeue Operation : ")
queue.dequeue()
queue.traverse()
print("**************************")

print("Dequeue Operation : ")
queue.dequeue()
queue.traverse()
print("**************************")


print("Dequeue Operation : (queue should be empty) ")
queue.dequeue()
queue.traverse()
print("**************************")

