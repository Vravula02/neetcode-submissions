class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n=len(coins)

        if n==0:
            return 0

        dp=[[-1]*(amount+1) for _ in range(n)]

        return self.helper(n-1,amount,dp,coins)
    
    def helper(self,ind,target,dp,coins):

        if ind==0:
            if target%coins[0]==0:
                return 1
            else:
                return 0

        if dp[ind][target]!=-1:
            return dp[ind][target]

        notTake=self.helper(ind-1,target,dp,coins)
        take=self.helper(ind,target-coins[ind],dp,coins) if target>=coins[ind] else 0

        dp[ind][target]=take+notTake
        return dp[ind][target]