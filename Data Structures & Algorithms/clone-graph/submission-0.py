"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        self.mpp={}

        return self.dfs(node)
    
    def dfs(self,node):

        if node in self.mpp:
            return self.mpp[node]
        
        copy=Node(node.val)
        self.mpp[node]=copy

        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor))
        return copy
