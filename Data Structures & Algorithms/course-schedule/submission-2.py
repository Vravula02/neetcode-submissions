class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=collections.defaultdict(list)

        for u,v in prerequisites:
            graph[v].append(u)

        return numCourses==len(self.topoSort(graph,numCourses))
        
    def topoSort(self,graph,numCourses):

        n=numCourses

        indegree=[0]*n

        for node in graph:
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
