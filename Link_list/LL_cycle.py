""" Leetcode -Linked_list Cycle -141
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list."""#  Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =None

    def append(self, x):
        if not self.head:
            self.head =ListNode(x)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next    
            curr.next = ListNode(x)    

    def create_cycle(self, pos):
        if pos == -1:
            return
        curr = self.head
        cycle_node = None
        last_node = None
        index = 0
        while curr:
            if index == pos:
                cycle_node = curr
            last_node = curr    
            index += 1
            curr = curr.next
        if last_node:
            last_node.next = cycle_node    



class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True  
            
        return False

# Create the Linked List    
linked_list = LinkedList()
values = [3, 2, 0, -4]      
for value in values:
    linked_list.append(values[value])

# Create a cycle in the link list    
pos = 1 # The index of the node that last node should link back
linked_list.create_cycle(pos)

# Check for cycle using the solution.
solution = Solution()
print(solution.hasCycle(linked_list.head)) # Should print true because there is cycle.