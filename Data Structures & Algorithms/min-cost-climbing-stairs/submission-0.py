class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n=len(cost)
        dp=[-1]*(n)

        return min(self.helper(n-1,cost,dp),self.helper(n-2,cost,dp))

    
    def helper(self,ind,cost,dp):

        if ind<=1:
            dp[ind]=cost[ind]
            return dp[ind]
        
        if dp[ind]!=-1:
            return dp[ind]

        oneStep=self.helper(ind-1,cost,dp)
        twoStep=self.helper(ind-2,cost,dp)

        dp[ind]=cost[ind]+min(oneStep,twoStep)
        return dp[ind]

