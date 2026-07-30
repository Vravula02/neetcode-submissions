# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None
        first=head

        second=self.reverse(second)
        dummy=ListNode(-1)
        temp=dummy

        while first and second:
            temp.next=first
            first=first.next
            temp=temp.next

            temp.next=second
            second=second.next
            temp=temp.next
        
        if first:
            temp.next=first
        
        


    
        
    def reverse(self,head):

        prev=None
        curr=head

        while curr:
            front=curr.next
            curr.next=prev

            prev=curr
            curr=front
        
        return prev