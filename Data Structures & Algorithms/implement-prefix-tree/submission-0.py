class Node:

    def __init__(self):
        self.links=[None]*26
        self.flag=False
    
    def containsKey(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    
    def put(self,ch):
        self.links[ord(ch)-ord('a')]=Node()
    
    def getNext(self,ch):
        return self.links[ord(ch)-ord('a')]
    
    def isEnd(self):
        return self.flag
    
    def setEnd(self):
        self.flag=True



class PrefixTree:

    def __init__(self):
        self.root=Node()
        

    def insert(self, word: str) -> None:
        node=self.root

        for ch in word:
            if not node.containsKey(ch):
                node.put(ch)
            node=node.getNext(ch)
        node.setEnd()


    def search(self, word: str) -> bool:

        node=self.root

        for ch in word:
            if not node.containsKey(ch):
                return False
            node=node.getNext(ch)
        return node.isEnd()
        

    def startsWith(self, prefix: str) -> bool:

        node=self.root

        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node=node.getNext(ch)
        return True
        
        
        