class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        ans=[]

        items=list(freq.items())

        items.sort(key=lambda x:x[1],reverse=True)

        for i in range(k):
            ans.append(items[i][0])
        
        return ans
