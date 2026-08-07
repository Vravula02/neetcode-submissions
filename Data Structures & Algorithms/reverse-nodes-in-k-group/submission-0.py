# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp=head
        lastNode=None

        while temp:

            kthNode=self.kthNode(k,temp)

            if not kthNode:
                if lastNode:
                    lastNode.next=temp
                break
            
            nextNode=kthNode.next
            kthNode.next=None

            newHead=self.reverse(temp)

            if lastNode:
                lastNode.next=newHead
            else:
                head=newHead
            
            temp.next=nextNode

            lastNode=temp
            temp=nextNode
        
        return head

        

    def kthNode(self,k,head):

        temp=head

        while temp and k>1:
            temp=temp.next
            k-=1
        return temp
    
    
    def reverse(self,head):

        prev=None
        curr=head

        while curr:
            front=curr.next
            curr.next=prev

            prev=curr
            curr=front
        
        return prev

