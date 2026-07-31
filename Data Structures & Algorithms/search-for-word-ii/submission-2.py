class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie=Trie()

        for word in words:
            trie.add(word)
        
        self.ans=[]

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i,j,board,"",trie.root)
        return self.ans

    def dfs(self,i,j,board,path,node):

        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]=="#":
            return

        ch=board[i][j]        
        if not node.containsKey(ch):
            return
        
        path+=ch
        node=node.getNext(ch)

        if node.isEnd():
            self.ans.append(path)
            node.flag=False
        board[i][j]="#"

        self.dfs(i+1,j,board,path,node)
        self.dfs(i-1,j,board,path,node)
        self.dfs(i,j+1,board,path,node)
        self.dfs(i,j-1,board,path,node)

        board[i][j]=ch


class Trie():

    def __init__(self):
        self.root=Node()
    
    def add(self,word):

        node=self.root

        for ch in word:
            if not node.containsKey(ch):
                node.put(ch)
            node=node.getNext(ch)
        node.setEnd()

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
