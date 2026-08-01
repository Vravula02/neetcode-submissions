class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph=[[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()
        count=0

        for node in range(n):

            if node not in visited:
                count+=1
                self.dfs(node,graph,visited)
        return count

    def dfs(self,node,graph,visited):

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor,graph,visited)
        