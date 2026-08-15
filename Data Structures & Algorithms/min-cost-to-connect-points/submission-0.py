class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges=[]


        for i in range(len(points)):
            x1,y1=points[i][0],points[i][1]

            for j in range(i+1,len(points)):

                x2,y2=points[j]

                dist=abs(x1-x2)+abs(y1-y2)
                edges.append([dist,i,j])
        
        edges.sort(key=lambda x:x[0])
        res=0
        ds=DisjointSet(len(points))

        for dist,u,v in edges:

            if not ds.find(u,v):
                ds.union(u,v)
                res+=dist
        return res


        

class DisjointSet:

    def __init__(self,n):
        self.rank=[0]*n
        self.parent=[i for i in range(n)]
    
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

        if self.rank[upU]>self.rank[upV]:
            self.parent[upV]=upU
        elif self.rank[upV]>self.rank[upU]:
            self.parent[upU]=upV
        else:
            self.parent[upV]=upU
            self.rank[upU]+=1