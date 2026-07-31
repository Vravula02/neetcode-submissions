class WordDictionary:

    def __init__(self):
        self.trie=Trie()        

    def addWord(self, word: str) -> None:

        node=self.trie.root

        for ch in word:
            if not node.containsKey(ch):
                node.put(ch)
            node=node.getNext(ch)
        node.setEnd()

    def search(self, word: str) -> bool:

        def dfs(ind,node):
            
            if ind==len(word):
                return node.isEnd()

            if word[ind]==".":
                for link in node.links:

                    if link:
                        if dfs(ind+1,link):
                            return True
                return False
            else:
                if not node.containsKey(word[ind]):
                    return False
                node=node.getNext(word[ind])
                return dfs(ind+1,node)

        return dfs(0,self.trie.root)
class Trie:

    def __init__(self):
        self.root=Node()

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
    
    def setEnd(self):
        self.flag=True
    
    def isEnd(self):
        return self.flag
        
