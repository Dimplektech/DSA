class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def enqueue(self, Value):

        new_node = Node(Value)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node  

    def dequeue(self):

        if self.front == None:
            return "Empty" 
        else:
            self.front = self.front.next

    def is_empty(self):
        return print(self.front == None)
    
    def size(self):
        curr = self.front
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count    
    
    def front_peek(self):
        if self.front == None:
            return "Empty"
        else:
            return self.front.data

    def rear_peek(self):
        if self.rear == None:
            return "Empty"
        else:
            return self.rear.data

    def traverse(self):
        curr = self.front

        while curr:
            print(curr.data)
            curr = curr.next


q = Queue()

q.enqueue(4)
q.enqueue(5)
q.enqueue(7)
q.enqueue(8)

# q.traverse() # Output will be 4 5 7 8 as insertion is from tail
# print("**************************************************")
# q.dequeue() # It will delete 4 as deletion happens from front or head.
# q.traverse()
# print("**************************************************")
# q.dequeue() # It will delete 4 as deletion happens from front or head.
# q.traverse()
# print("**************************************************")
# q.dequeue() # It will delete 4 as deletion happens from front or head.
# q.traverse()
# print("**************************************************")
# q.dequeue() # It will delete 4 as deletion happens from front or head.
q.traverse()
q.is_empty()
print(q.size())
print(q.rear_peek())
print(q.front_peek())
