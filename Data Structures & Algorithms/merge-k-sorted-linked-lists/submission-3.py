# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        pq=[]

        for l in lists:

            curr=l
            while curr:
                heapq.heappush(pq,curr.val)
                curr=curr.next
        
        dummy=ListNode(-1)
        temp=dummy

        while pq:

            nodeVal=heapq.heappop(pq)
            temp.next=ListNode(nodeVal)
            temp=temp.next
        
        return dummy.next



