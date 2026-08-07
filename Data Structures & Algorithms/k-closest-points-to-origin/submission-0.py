class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pq=[]

        for point in points:

            dist=math.sqrt((point[0]**2)+(point[1]**2))

            if len(pq)<k:
                heapq.heappush(pq,(-dist,(point[0],point[1])))
            else:
                heapq.heappushpop(pq,(-dist,(point[0],point[1])))
        
        res=[]

        for ele in pq:
            dist,coor=ele
            x,y=coor

            res.append([x,y])

        return res

        