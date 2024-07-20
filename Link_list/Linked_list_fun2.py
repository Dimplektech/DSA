""" Given a linked list of characters. Write python function to return a new
 string that created by appending all the characters given in the linked list 
  as per the rules given below.
    
Rules->
# Replace '*' or '/' by a single space
# In case of two consecutive occurance of '*' or '/' ,replace those two
# occurrences by single space and covert the next character to upper case.

# Assume that ->
# There will not be more than two consecutive occurance of '*' or '/'
# The linked list will always end with an alphabet.
# 
# Sample Input
#  The/*sky*is//blue

# Expected output
# The Sky is Blue 
# """

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, data):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = new_node


    def print(self):
        if self.head is None:  
            print("Linked List is empty")  
            return
        
        curr = self.head
        llstr = ''
        while curr:
            llstr += str(curr.data) 
            curr = curr.next
            
        print(llstr) 

    ### Replace / *
    def change_sentence(self):
        curr = self.head
        while curr:
            if curr.data == '/' or curr.data == '*':
                curr.data = ' '
                if curr.next.data == '/' or curr.next.data == '*':
                    if curr.next.next:
                        curr.next.next.data = curr.next.next.data.upper()
                    curr.next = curr.next.next
                else:
                    curr = curr.next
            else:
                curr = curr.next        





L = LinkedList()        
L.add("T")
L.add("h")
L.add("e")
L.add("/")
L.add("*")
L.add("s")
L.add("k")
L.add("y")
L.add("*")
L.add("i")
L.add("s")
L.add("/")       
L.add("/")
L.add("b")
L.add("l")
L.add("u")
L.add("e")

L.print()   
L.change_sentence()
L.print()