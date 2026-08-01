class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        dp=[-1]*(n)

        return self.helper(n-1,nums,dp)
    
    def helper(self,ind,nums,dp):

        if ind==0:
            dp[0]=nums[0]
            return dp[0]
        
        if ind==1:
            dp[ind]=max(nums[0],nums[1])
            return dp[ind]
        
        if dp[ind]!=-1:
            return dp[ind]
        
        nonPick=self.helper(ind-1,nums,dp)
        pick=self.helper(ind-2,nums,dp)+nums[ind]

        dp[ind]=max(nonPick,pick)
        return dp[ind]