'''Doubly Link List '''
'''Print Forward list and print Backword list'''


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkList:
    
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self):
        if self.head is None:
            print("List is empty")        
        else:
            linkstr = ''
            itr = self.head
            while itr.next:
                linkstr += str(itr.next.data) + "-->"
                
                itr = itr.next
        print(linkstr)
   
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            counnt += 1
            itr = itr.next
        return count
    
    def get_last_node(self):  # Function to get last node of the list.

        itr = self.head
        while itr.next:
            itr = itr.next
        return itr    
              
    def print_backwards(self): #  Function to print LinkList Backwards.
        if self.head is None:
            print("List is empty")
            return       
    
        last_node = self.get_last_node()
        itr = last_node
        linkstr = ''
        
        while itr.prev:
            linkstr += str(itr.data) + "-->"
            
            itr = itr.prev
        print(linkstr)

    def print(self):
        if self.head is None:
            print("List is empty")

        etr = self.head
        link_lst_str = ''
        while etr:
            link_lst_str += str(etr.data) + '-->'
            etr = etr.next
        print(link_lst_str)    


if __name__ == "__main__":
    
    l1 = DoublyLinkList()
    l1.insert_values([45, 20, 30, 35, 21, 12])
    print("Forward List")
    l1.print_forward()
    print("Backward List")
    l1.print_backwards()
    
