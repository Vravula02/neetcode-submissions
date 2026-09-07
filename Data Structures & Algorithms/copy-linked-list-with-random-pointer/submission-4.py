"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        
        curr=head

        while curr:
            front=curr.next
            copy=Node(curr.val)
            curr.next=copy
            

            copy.next=front
            curr.next=copy

            curr=front
        
        newHead=head.next

        curr=head
        while curr:
            copy=curr.next

            if curr.random:
                copy.random=curr.random.next
            curr=copy.next
    
        curr=head

        while curr:
            copy=curr.next
            front=copy.next

            if front:
                copy.next=front.next
            curr.next=front
            curr=front
        return newHead


        