class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0

        dp=[-1]*(len(nums)+1)

        return self.helper(len(nums)-1,dp,nums)
    
    def helper(self,ind,dp,nums):

        if ind==0:
            return nums[0]
        
        if ind==1:
            return max(nums[0],nums[1])
        
        if dp[ind]!=-1:
            return dp[ind]
        
        nonPick=self.helper(ind-1,dp,nums)
        pick=self.helper(ind-2,dp,nums)+nums[ind] if ind>=2 else 0

        dp[ind]=max(pick,nonPick)
        return dp[ind]
        