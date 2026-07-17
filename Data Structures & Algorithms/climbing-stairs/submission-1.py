class Solution:
    def climbStairs(self, n: int) -> int:

        dp=[-1]*(n+1)

        return self.helper(n,dp)
    

    def helper(self,ind,dp):

        if ind<2:
            return 1
        
        if dp[ind]!=-1:
            return dp[ind]
        
        dp[ind]=self.helper(ind-1,dp)+self.helper(ind-2,dp)
        return dp[ind]
        

        