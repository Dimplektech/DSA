""" 
Using Stack
Write program to know whether anyone out of them, who is celebrity.
    A  B  C  D
A  [0, 0, 1, 1]
B  [0, 0, 1, 0]
C  [0, 0, 0, 0]
D  [0, 0, 1, 0]

Matrix to know whether they know each other
conditions are 
1. Clebrity doesnt know anyone which shows by 0 , then only he is celebrity
2. If person knows anyone that is represented by 1 , then he is not celebrity"""

# 2D List
L= [
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]


class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def push(self, data):
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

    def pop(self):
        
        popped_value = self.top
        self.top = self.top.next
        return popped_value.data

def find_the_celeb(L):

    s = Stack()

    for i in range(len(L)):
        s.push(i)  # Pushing no of rows only

    s.traverse()    

    while s.size() >= 2: # If stack size is >= 2 then only we are poping out
        # to item to compare
    
        i = s.pop()
        j = s.pop()
        """ Here we are selecting to items from stack checking if they are not 
        celebrity,elemeting them and adding rest one in stack again"""
        if L[i][j] == 0:  # checking by rows and columns
            # means J is not celebrity
            s.push(i)    
        else: # L[i][J] == 1
            #means I is not celebrity
            s.push(j)
        """When only one item left in stack we will add in celebs  and will 
        check for that person, all celebrity conditions"""
        celebs = s.pop()

    for i in range(len(L)):
        if i != celebs:
            """L[i][celebs] ==0 means i person doesn't know celebs means he is
              not celebrity
               L[celebs][i] ==1 means Celebs knows tht person 'i', means he is 
               not celebrity as celebs is not supposed to know anyone.
               if person doesnt know  and everyone knows him anyone means
               he is celebrity.
            """
            if L[i][celebs] == 0 or L[celebs][i] == 1:
                return ("No one is a Celebrity")
    
    print("The celebrity is", celebs)
                




find_the_celeb(L)     





