class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n=len(edges)

        ds=DisjointSet(n)
        
        for u,v in edges:
            if ds.find(u,v):
                return [u,v]
            
            ds.union(u,v)
    
class DisjointSet:

    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
    
    def findUPar(self,node):

        if self.parent[node]==node:
            return node
        
        self.parent[node]=self.findUPar(self.parent[node])
        return self.parent[node]
    
    def find(self,u,v):
        return self.findUPar(u)==self.findUPar(v)
    
    def union(self,u,v):

        upU=self.findUPar(u)
        upV=self.findUPar(v)

        if upU==upV:
            return
        
        if self.rank[upU]>self.rank[upV]:
            self.parent[upV]=upU
        elif self.rank[upV]>self.rank[upU]:
            self.parent[upU]=upV
        else:
            self.parent[upV]=upU
            self.rank[upU]+=1
        