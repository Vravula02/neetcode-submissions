class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[[-1]*(amount+1) for _ in range(len(coins))]

        ans=self.helper(len(coins)-1,amount,dp,coins)

        return ans if ans!=float('inf') else -1

    def helper(self,ind,target,dp,coins):

        if target==0:
            return 0
        
        if ind==0:
            return target//coins[0] if target%coins[0] ==0 else float('inf')

        if dp[ind][target]!=-1:
            return dp[ind][target]
        
        nonPick=self.helper(ind-1,target,dp,coins)
        pick=1+self.helper(ind,target-coins[ind],dp,coins) if target>=coins[ind] else float('inf')

        dp[ind][target]=min(pick,nonPick)

        return dp[ind][target]