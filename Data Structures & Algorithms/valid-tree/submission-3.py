class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n>len(edges)+1:
            return False


        graph=[[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=[False]*n

        for node in range(n):

            if not visited[node]:
                if self.dfsLoop(node,visited,-1,graph):
                    return False
        return True
        
        
    def dfsLoop(self,node,visited,parent,graph):

        visited[node]=True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if self.dfsLoop(neighbor,visited,node,graph):
                    return True
            elif parent!=neighbor:
                return True
        return False
        
