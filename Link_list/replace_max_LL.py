""" 1. Replace Maximum Number with Given Value
    2. Additin of odd numbers in the LinkedList
    3.LinkedList Inplace reversal (without making another LL,Reverse the LL)"""  


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None     

    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node    

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

    """ Replace Maximum Number with Given Value"""    
    def replace_max(self, value):
        curr = self.head
        max = curr
        while curr:
            if curr.data > max.data:
                max = curr
            curr = curr.next
        max.data = value  

    """Additin of odd numbers in the LinkedList"""    
    def add_odds(self):
        curr = self.head
        sum_odd = 0 
        while curr:
            if int(curr.data) % 2 != 0:
                sum_odd += curr.data
            curr = curr.next    
        return sum_odd        
    

    """ LinkedList Inplace reversal (without making another LL,Reverse the LL)"""
    def reverse_LL(self):
        prev_node = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node


L = LinkedList()
L.add(12)
L.add(21)
L.add(3)
L.add(45)
L.add(5)
L.print()
L.replace_max(20)
L.print()
L.reverse_LL()
L.print()
sum_odds = L.add_odds()
print("sum of odds", sum_odds)
