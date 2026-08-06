class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low=1
        high=max(piles)

        while low<=high:

            k=(low+high)//2
            hours=self.timeTaken(piles,k)

            if hours>h:
                low=k+1
            else:
                high=k-1
        return low

    def timeTaken(self,piles,rate):

        res=0

        for pile in piles:
            res+=(pile//rate)
            if pile%rate!=0:
                res+=1
        return res

        