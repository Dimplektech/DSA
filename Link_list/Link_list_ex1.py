# Class for Node Element.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Class for Link List
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        link_list_str = ""
        while itr:
            link_list_str += str(itr.data) + "-->"
            itr = itr.next

        print(link_list_str)

    # Insert Node at the end of the list.
    def insert_at_end(self, data):
        if self.head is None:  # If head is none ,assign that node as head.
            self.head = Node(data, None)
        # if head is there in Linklist.
        else:
            itr = self.head  # Start with first element of Link List.
            while itr.next: # iterarte through linkList till it reaches to end node.
                itr = itr.next
            # When it doesn't have next node that means it reaches to the end node.   
            itr.next = Node(data, None)  # Assign Node to the Next to the last node.

    # Inserting new values in the list using insert_at_end function.
    def insert_values(self, data_list):
        self.head = None  # It Create new Fresh List.
        for data in data_list:
            self.insert_at_end(data)
    
    #  Function to get the length of the Link List.
    def get_lengh(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    # Function to remove element from the Link List.
    def remove_at(self, index):
        if index < 0 or index >= self.get_lengh():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return
        
        # Check for other Index
        count = 0
        itr = self.head
        while itr:  # Iterate through List.
            ''' when Count reaches to one Elemnt before index element,then
                assign 'next to next' element as 'next element' of current
                element (which is one element before index element). '''
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    # Function to insert element at the given index.
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_lengh():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head

        while itr:
            if count == index-1:
                ''' When count reaches to one element  before given index 
                    create new node by sending next element as argument and
                    set itr(current).next is equal to Node'''
                # Create Node.
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                self.insert_at(count+1, data_to_insert)

            itr = itr.next
            count = count  + 1
            

    def remove_by_value(self, data):
        if self.head is None:
            return 

        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
            itr = itr.next
            count += 1 


if __name__ == "__main__":
    l1 = LinkedList()
    # Insert at the begining of the LinkList.
    # l1.insert_at_begining(5)
    # l1.insert_at_begining(45)
    # l1.insert_at_begining(23)
    # l1.insert_at_begining(12)
    # # Insert at end of the Link List
    # l1.insert_at_end(10)
    # l1.insert_at_end(89)
    # l1.insert_at_end(57)
    # l1.print()
    
    # Insert New Vlaues in the linklist.
    l1.insert_values(["Banana", "Apple", "Strawberry", "Pear"])
    
    # Print Length of the Link List.
#     print("Length of my Link List is : ", l1.get_lengh())
   
#     # Remove Element from the LinkList.
#     l1.remove_at(2)
#     l1.print()
#     l1.insert_at(1, "Strawberry")
#     l1.insert_at(0, "Peach")
#   #  l1.insert_at(9, "Strawberry")
    l1.print()
    l1.insert_after_value("Apple", "Mango")
    l1.print()
    l1.remove_by_value("Strawberry")
    l1.print()
    l1.remove_by_value("Pear")
    l1.remove_by_value("Apple")
    l1.remove_by_value("Mango")
    l1.print()

