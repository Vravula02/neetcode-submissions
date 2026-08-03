class Solution:
    def countBits(self, n: int) -> List[int]:

        res=[]

        for num in range(n+1):
            res.append(self.ones(num))

        return res
        
    def ones(self,n):

        count=0

        for _ in range(32):

            count+=(1&n)
            n=n>>1
        return count