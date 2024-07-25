""" Queue recursion"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # In queue we enqueue data from rear.
    def enqueue(self, value):
        new_node = Node(value)

        if self.rear == None:
            # If queueis empty then assisgn front and rear to new node.
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node

    # In queue we pop data from front.
    def dequeue(self):
        if self.rear == None:
            return "Empty queue"
        else:
            popped_item = self.front
            self.front = self.front.next
            return popped_item.data
        
    def is_empty(self):
        return self.front == None


### Find result using recursion
que = Queue()


def fun(num):
    if (num == 0):
        return 0
    else:
        que.enqueue(num % 10)
        res = fun(num//10) 
        res = res * 10 + int(que.dequeue())
        return res


print(fun(123))







