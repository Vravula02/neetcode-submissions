class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        withStart=nums[:-1]
        withEnd=nums[1:]
        n=len(nums)-1

        dp1=[None]*n
        dp2=[None]*n

        return max(self.helper(n-1,withStart,dp1),self.helper(n-1,withEnd,dp2))

    
    def helper(self,ind,nums,dp):

        if ind==0:
            dp[ind]=nums[0]
            return dp[0]
        if ind==1:
            dp[ind]=max(nums[0],nums[1])
            return dp[ind]
        
        if dp[ind]!=None:
            return dp[ind]
        
        nonPick=self.helper(ind-1,nums,dp)
        pick=self.helper(ind-2,nums,dp)+nums[ind]

        dp[ind]=max(nonPick,pick)
        return dp[ind]
    
        