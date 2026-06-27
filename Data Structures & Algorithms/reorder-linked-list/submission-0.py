# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        middleNode=self.findMiddle(head)
        second=middleNode.next
        middleNode.next=None
        second=self.reverse(second)
        first=head

        dummyNode=ListNode(-1)
        res=dummyNode

        while first and second:
            res.next=first
            res=res.next
            first=first.next

            res.next=second
            res=res.next
            second=second.next
        
        if first:
            res.next=first
    
    def findMiddle(self,head):
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow

    
    def reverse(self,head):

        prev=None
        curr=head

        while curr:
            front=curr.next
            curr.next=prev

            prev=curr
            curr=front
        
        return prev