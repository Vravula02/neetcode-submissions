class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp=[[-1 for _ in range(amount+1)] for _ in range(len(coins))]

        res=self.helper(len(coins)-1,amount,coins,dp) 

        return res if res!=float("inf") else -1 


    def helper(self,ind,target,coins,dp):

        if target==0:
            return 0

        if ind==0:
            if target%coins[0]==0:
                return target//coins[0]
            else:
                return float('inf')
        
        if dp[ind][target]!=-1:
            return dp[ind][target]
        
        nonTake=self.helper(ind-1,target,coins,dp)
        take=1+self.helper(ind,target-coins[ind],coins,dp) if target>=coins[ind] else float('inf')

        dp[ind][target]=min(take,nonTake)
        return dp[ind][target]