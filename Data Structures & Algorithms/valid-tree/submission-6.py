class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges)!=n-1:
            return False
        visited=set()

        graph=[[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            if node not in visited:
                if self.dfs(0,graph,visited,-1):
                        return False
        return True
    
    def dfs(self,node,graph,visited,parent):

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if self.dfs(neighbor,graph,visited,node):
                    return True
            elif parent!=neighbor:
                return True
        