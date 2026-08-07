class Solution:
    def isHappy(self, n: int) -> bool:
        
        slow=n
        fast=self.sqSum(n)

        while slow!=fast:

            slow=self.sqSum(slow)
            fast=self.sqSum(self.sqSum(fast))
        
        return True if slow==1 else False


    
    def sqSum(self,n):

        res=0

        while n:

            digit=n%10
            res+=(digit**2)
            n=n//10
        return res