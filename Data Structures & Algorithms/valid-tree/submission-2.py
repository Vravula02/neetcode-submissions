class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        if len(edges) != n - 1:
            return False

        graph=[[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited=[False]*n

        for node in range(n):
            if not visited[node]:
                if self.dfs(node,-1,graph,visited):
                    return False
        
        for node in visited:
            if not node:
                return False
        return True
    
    def dfs(self,node,parent,graph,visited):

        visited[node]=True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor,node,graph,visited):
                    return True
            else:
                if parent!=neighbor:
                    return True 
        return False
        
