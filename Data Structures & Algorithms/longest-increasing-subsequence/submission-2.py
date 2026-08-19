class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n=len(nums)

        dp=[[-1 for _ in range(n+1)] for _ in range(n)]

        return self.helper(0,-1,dp,nums)
        
    def helper(self,ind,prevInd,dp,nums):

        if ind==len(nums)-1:
            if nums[prevInd]<nums[ind] or prevInd==-1:
                return 1
            else:
                return 0
        
        if dp[ind][prevInd+1]!=-1:
            return dp[ind][prevInd+1]
        
        notTaken=self.helper(ind+1,prevInd,dp,nums)
        taken=0

        if prevInd==-1 or nums[ind]>nums[prevInd]:
            taken=self.helper(ind+1,ind,dp,nums)+1
        
        dp[ind][prevInd+1]=max(taken,notTaken)

        return dp[ind][prevInd+1]

        
