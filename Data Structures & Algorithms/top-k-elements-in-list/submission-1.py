class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1
        
       
        ans=[]

        for num,count in freq.items():
            ans.append((count,num))
        
        ans.sort(key=lambda x:x[0], reverse=True)

        res=[]
        i=0

        while i<k:
            res.append(ans[i][1])
            i+=1
        
        return res