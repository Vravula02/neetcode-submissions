# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=None

        for lis in lists:
            res=self.merge(res,lis)
        return res
    
    def merge(self,first,second):

        dummyNode=ListNode(-1)
        temp=dummyNode

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
                
        