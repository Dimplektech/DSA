class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        # Empty linkedList
        self.head = None
        self.n = 0  # number of nodes in the linked list 

    def __len__(self):
        return self.n
    

    def insert_head(self, value):
        # craete new_node
        new_node = Node(value)
        # Create Connection
        new_node.next = self.head
        # Reassign head
        self.head = new_node
        # Increament n
        self.n += 1

    # Traverse
    def __str__(self):
        # Set Current cursor to head
        curr = self.head
        result = ''

        while curr != None:
            result = result + str(curr.value) + '->' # Print result ex. 4->3->2->1
            curr = curr.next  # Move cursor to next Node
        return result[:-2]

    def append(self, value):
        new_node = Node(value)
        if self.head == None:  # If List is empty then assign new node as head.
            self.head = new_node
        curr = self.head

        while curr.next != None:
            curr = curr.next
        # You are at the last Node.
        curr.next = new_node    
        self.n += 1

    def insert_after(self, after, value):
        # Create new_node
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.value == after:
                break
            curr = curr.next
        if curr != None:    
            new_node.next = curr.next
            curr.next = new_node    
            self.n += 1
        else:
            print("Item not Found")    

    ###############Delete Linked List####################
    # 1. Clear Linked |List
    def clear(self):
        self.head = None
        self.n = 0

    # 2. Delete head

    def delete_head(self):
        if self.head == None:
            return "Empty LL"
        
        self.head = self.head.next
        self.n -=1

    def delete_from_tail(self):
        if self.head == None: # If LL is empty
            return "Empty LL"
        curr = self.head
        if curr.next == None: #If only one item
            self.delete_head()
          
        else:
            while curr.next.next != None:
                curr = curr.next
            curr.next = None    
        self.n -= 1

    def remove(self, value):
        if not self.head:
            return "List is empty"

        # If head holds the value.
        if self.head.value == value:
            return self.delete_head()
            
        curr = self.head

        while curr.next != None:
            if curr.next.value == value:
                curr.next = curr.next.next
                self.n -= 1
                return True
            curr = curr.next

        return "Item not Found"
    ## Search
    def search(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.value == item:
                return pos
            curr = curr.next
            pos += 1
        
        return 'Not Found'
    
    #  Indexing
    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.value 
            curr = curr.next
            pos += 1


L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.append(5)
L.insert_after(1, 30)

print(len(L))
print(L)
L.delete_head()
print(L)
# L.clear()
# print("Cleared LinkedList")
L.delete_from_tail()
print(L)
# L.delete_from_tail()
# print(L)
# L.delete_from_tail()
# print(L)
# L.delete_from_tail()
# print(L)
# L.delete_from_tail()
# print(L)
L.remove(10)
print(L)
print(L.search(2))
print(L.__getitem__(80))