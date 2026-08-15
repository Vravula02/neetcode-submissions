class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph=[[] for _ in range(n)]

        for u,v,ct in flights:
            graph[u].append((v,ct))

        cost=[float('inf')]*n

        cost[src]=0

        q=[(0,src,0)]

        while q:

            currCost,node,stops=q.pop(0)
            
            if stops>k:
                continue
            
            for neighbor,wt in graph[node]:

                if cost[neighbor]>wt+currCost:
                    cost[neighbor]=wt+currCost
                    q.append((cost[neighbor],neighbor,stops+1))
        
        return -1 if cost[dst]==float('inf') else cost[dst]