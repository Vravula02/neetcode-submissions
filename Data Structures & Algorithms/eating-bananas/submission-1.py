class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low=1
        high=max(piles)

        while low<=high:
            rate=(low+high)//2

            hours=self.timeTaken(piles,rate)

            if hours>h:
                low=rate+1
            else:
                high=rate-1
        return low

        
    
    def timeTaken(self,piles,k):

        hours=0

        for pile in piles:
            hours+=(pile//k)

            if pile%k!=0:
                hours+=1
        return hours