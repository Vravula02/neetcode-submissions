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

        self.insertRandomNodes(head)
        self.insertRandomPointers(head)
        return self.removeConnections(head)
    
    def insertRandomNodes(self,head):

        dummyNode=Node(-1)
        dummy=dummyNode

        temp=head

        while temp:
            front=temp.next
            newNode=Node(temp.val)

            temp.next=newNode
            newNode.next=front

            temp=front
    
    def insertRandomPointers(self,head):

        temp=head
        dummy=head.next

        while temp:

            if temp.random:
                dummy.random=temp.random.next
            else:
                dummy.random=None

            temp=dummy.next
            dummy=temp.next if temp else None
    
    def removeConnections(self,head):

        temp=head
        dummyNode=Node(-1)
        res=dummyNode
        res.next=temp
        

        while temp:
            res.next=temp.next
            res=res.next

            temp.next=res.next
            temp=temp.next
        return dummyNode.next

