class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph=[[] for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[v].append(u)
        
        topo=self.topoSort(numCourses,graph)

        if len(topo)!=numCourses:
            return []
        return topo

    def topoSort(self,n,graph):

        indegree=[0]*n

        for node in range(len(graph)):
            for neighbor in graph[node]:
                indegree[neighbor]+=1
        
        dq=collections.deque()

        for i in range(len(indegree)):
            if indegree[i]==0:
                dq.append(i)

        res=[]
        while dq:

            node=dq.popleft()
            res.append(node)

            for neighbor in graph[node]:
                indegree[neighbor]-=1

                if indegree[neighbor]==0:
                    dq.append(neighbor)
        return res


        