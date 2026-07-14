class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph=[[] for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[v].append(u)

        topo=self.topoSort(graph)

        return len(topo)==numCourses
        
    def topoSort(self,graph):
        n=len(graph)

        indegree=[0]*n

        for u in range(n):
            for v in graph[u]:
                indegree[v]+=1
        
        dq=collections.deque()
        
        for node in range(n):
            if indegree[node]==0:
                dq.append(node)

        topo=[]
        while dq:

            node=dq.popleft()
            topo.append(node)

            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    dq.append(neighbor)
        return topo
        
