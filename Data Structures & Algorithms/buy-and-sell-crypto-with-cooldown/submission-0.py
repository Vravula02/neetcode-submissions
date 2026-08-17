class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        dp=[[-1]*2 for _ in range(n+1)]

        return self.helper(0,0,prices,dp)

    
    def helper(self,ind,buy,prices,dp):

        if ind>=len(prices):
            return 0
        
        if dp[ind][buy]!=-1:
            return dp[ind][buy]
        
        if buy==0:
            get=self.helper(ind+1,1,prices,dp)-prices[ind]
            dontGet=self.helper(ind+1,0,prices,dp)

            dp[ind][buy]=max(get,dontGet)
        else:
            sell=self.helper(ind+2,0,prices,dp)+prices[ind]
            dontSell=self.helper(ind+1,1,prices,dp)

            dp[ind][buy]=max(sell,dontSell)
        
        return dp[ind][buy]

            