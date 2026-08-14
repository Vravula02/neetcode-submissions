class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n=len(edges)
        graph=[[] for _ in range(n+1)]
        indegree=[0]*(n+1)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        
        dq=collections.deque()

        for i in range(1,n+1):
            if indegree[i]==1:
                dq.append(i)
        
        while dq:

            node=dq.popleft()
            indegree[node]-=1

            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==1:
                    dq.append(neighbor)
        
        for u,v in reversed(edges):
            if indegree[u]>0 and indegree[v]>0:
                return [u,v]
