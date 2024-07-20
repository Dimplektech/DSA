class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None        
        
    def insert_at_begining(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            
            self.insert_at_end(data)

    def print(self):
        if self.head is None:  
            print("Linked List is empty")  
            return
        
        curr = self.head
        llstr = ''
        while curr:
            llstr += str(curr.data) + '-->'
            curr = curr.next
            
        print(llstr[:-3]) 

    def get_length(self):
        if self.head is None:
            return "LinkedList is empty"
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        return count    
    
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        count = 0
        while curr:
            if count == index -1:
                curr.next= curr.next.next

            curr = curr.next
            count += 1

    def insert_at(self, index, data):
        
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")


        if index == 0:
            self.insert_at_begining(data)
            return
        new_node = Node(data)
        curr = self.head
        count = 0
        while curr != None:
            if count == index-1:
                new_node.next = curr.next
                curr.next = new_node
            curr = curr.next
            count = count + 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return "LinkedList is empty."
        

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
         
        curr = self.head
        while curr:
            if curr.data == data_after:
                #new_node.next = curr.next
                curr.next = Node(data_to_insert, curr.next)
                break
          
            curr = curr.next
      
    def remove_by_value(self, data):
        if self.head == None:
            return " List is empy."
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                # If the node to be removed is the last node.
                if curr.next.next is None:
                    curr.next = None
                else:    
                    curr.next = curr.next.next
                return    
            curr = curr.next    



if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_begining(10)
    l1.insert_at_begining(20)
    l1.insert_at_begining(30)
    l1.insert_at_begining(40)
    l1.insert_at_begining(50)
    l1.print()
    # l1.insert_at_end(100)
    # l1.print()
    # l1.insert_values(["apple", "banana", "orange", "grapes"])
    # l1.print()
    # print(l1.get_length())
    # # l1.remove_at(2)

    # l1.insert_at(0, "mango")
    # l1.print()
    l1.insert_after_value(30, 23)
    l1.print()
    l1.remove_by_value(30)
    l1.print()
    l1.remove_by_value(10)
    l1.print()

    