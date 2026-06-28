# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode=ListNode(-1)
        temp=dummyNode
        first,second=list1,list2

        while first and second:

            if first.val<=second.val:
                temp.next=first
                first=first.next
            else:
                temp.next=second
                second=second.next
            temp=temp.next
        
        if first:
            temp.next=first
        
        if second:
            temp.next=second
        
        return dummyNode.next