class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        
        items=[(key,val) for key,val in freq.items()]

        items.sort(key=lambda x:x[1],reverse=True)

        res=[]
        for item in items:
            if len(res)<k:
                res.append(item[0])
        return res