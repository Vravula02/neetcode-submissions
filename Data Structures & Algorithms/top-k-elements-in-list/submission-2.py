class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1
        
       
        pq=[]

        for num,count in freq.items():

            if len(pq)<k:
                heapq.heappush(pq,(count,num))
            else:
                heapq.heappushpop(pq,(count,num))
        return [num for count,num in pq]