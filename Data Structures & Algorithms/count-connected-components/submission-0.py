class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph=[[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        
        count=0
        visited=[0]*n

        for node in range(n):
            if visited[node]==0:
                visited[node]=1
                count+=1
                self.dfs(node,graph,visited)
        return count
    
    def dfs(self,node,graph,visited):

        for neighbor in graph[node]:
            if visited[neighbor]==0:
                visited[neighbor]=1
                self.dfs(neighbor,graph,visited)