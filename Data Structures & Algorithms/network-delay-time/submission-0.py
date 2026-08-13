class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        dist=[float('inf')]*(n+1)

        graph=[[] for i in range(n+1)]

        dist[k]=0

        for u,v,t in times:
            graph[u].append((v,t))
        
        dq=collections.deque([(0,k)])

        while dq:

            t,node=dq.popleft()

            for neighbor,prevTime in graph[node]:
                if dist[neighbor]>t+prevTime:
                    dist[neighbor]=t+prevTime
                    dq.append((dist[neighbor],neighbor))
        ans=max(dist[1:])

        return ans if ans!=float("inf") else -1


        
