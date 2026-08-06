class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.pq=[]
        self.k=k

        for num in nums:
            if len(self.pq)<self.k:
                heapq.heappush(self.pq,num)
            else:
                heapq.heappushpop(self.pq,num)

    def add(self, val: int) -> int:

        if len(self.pq)<self.k:
            heapq.heappush(self.pq,val)
        else:
            heapq.heappushpop(self.pq,val)
        return self.pq[0]  
        
