class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        excludeLast=nums[:-1]
        excludeFirst=nums[1:]

        dp1=[-1]*(len(nums)-1)
        dp2=[-1]*(len(nums)-1)

        return max(self.helper(len(nums)-2,dp1,excludeLast),self.helper(len(nums)-2,dp2,excludeFirst))
    
    def helper(self,ind,dp,nums):

        if ind<0:
            return 0

        if ind==0:
            dp[ind]=nums[0]
            return dp[ind]
        
        if dp[ind]!=-1:
            return dp[ind]
        
        nonPick=self.helper(ind-1,dp,nums)
        pick=self.helper(ind-2,dp,nums)+nums[ind]

        dp[ind]=max(pick,nonPick)
        return dp[ind]