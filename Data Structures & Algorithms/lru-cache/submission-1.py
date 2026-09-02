class Node:

    def __init__(self,key=0,val=0,next=None,prev=None):
        self.key=key
        self.val=val
        self.next=next
        self.prev=prev

class LRUCache:

    def __init__(self, capacity: int):

        self.cap=capacity
        self.mpp={}
        self.head=Node()
        self.tail=Node()

        self.head.next=self.tail
        self.tail.prev=self.head   

    def _insert_at_front(self,node):

        front=self.head.next

        self.head.next=node
        node.prev=self.head

        node.next=front
        front.prev=node

    def _remove(self,node):

        back=node.prev
        front=node.next

        back.next=front
        front.prev=back    

    def get(self, key: int) -> int:

        if key not in self.mpp:
            return -1
        
        node=self.mpp[key]

        self._remove(node)
        self._insert_at_front(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.mpp:
            node=self.mpp[key]
            node.val=value

            self._remove(node)
            self._insert_at_front(node)

            return
        
        if len(self.mpp)==self.cap:

            lru_node=self.tail.prev

            self._remove(lru_node)
            del self.mpp[lru_node.key]
        
        node=Node(key,value)
        self.mpp[key]=node

        self._insert_at_front(node)
