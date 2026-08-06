class Node:

    def __init__(self,key,val,next=None,prev=None):
        self.key,self.val=key,val
        self.next,self.prev=next,prev

class LRUCache:

    def __init__(self, capacity: int):

        self.cap=capacity
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.mpp={}

    def removeNode(self,node):

        back=node.prev
        front=node.next

        back.next=front
        front.prev=back

    def insertNode(self,node):

        front=self.head.next
        node.next=front
        self.head.next=node

        node.prev=self.head
        front.prev=node

    def get(self, key: int) -> int:

        if key not in self.mpp:
            return -1
        
        self.removeNode(self.mpp[key])
        self.insertNode(self.mpp[key])

        return self.mpp[key].val

    def put(self, key: int, value: int) -> None:

        if key in self.mpp:
            self.mpp[key].val=value
            self.removeNode(self.mpp[key])
            self.insertNode(self.mpp[key])
        else:
            node=Node(key,value)
            self.mpp[key]=node
            self.insertNode(node)
        
        if len(self.mpp)>self.cap:
            last=self.tail.prev
            self.removeNode(last)
            del self.mpp[last.key]




