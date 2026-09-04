class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        pq=[]

        for num in nums:
            if len(pq)<k:
                heapq.heappush(pq,num)
            else:
                heapq.heappushpop(pq,num)
        return pq[0]
        