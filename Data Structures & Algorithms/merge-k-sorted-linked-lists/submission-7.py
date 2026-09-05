# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        pq=[]

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq,(lists[i].val,i,lists[i]))
        
        dummy=ListNode()
        curr=dummy

        while pq:

            val,i,node=heapq.heappop(pq)

            curr.next=node
            curr=curr.next

            if node.next:
                heapq.heappush(pq,(node.next.val,i,node.next))

        return dummy.next                    

        

        
