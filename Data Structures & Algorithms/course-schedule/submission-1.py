class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph=[[] for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[v].append(u)

        return len(self.topoSort(graph))==numCourses
        
    def topoSort(self,graph):

        indegree=[0]*len(graph)

        for node in range(len(graph)):
            for neighbor in graph[node]:
                indegree[neighbor]+=1
        
        dq=collections.deque()

        for node in range(len(indegree)):
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
