# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        pq=[]

        for ind,node in enumerate(lists):

            if node:
                heapq.heappush(pq,(node.val,ind,node))
        
        dummy=ListNode(-1)
        temp=dummy

        while pq:

            _,ind,node=heapq.heappop(pq)

            temp.next=node
            temp=temp.next

            if node.next:
                heapq.heappush(pq,(node.next.val,ind,node.next))
        return dummy.next

