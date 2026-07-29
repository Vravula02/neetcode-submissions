class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit=0
        mini=prices[0]

        for i in range(1,len(prices)):
            mini=min(mini,prices[i])
            profit=max(profit,prices[i]-mini)
        
        return profit