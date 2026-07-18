class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        total=sum(nums)

        if (total+target)%2==1:
            return 0

        s1=(total+target)//2

        dp=[[-1]*(s1+1) for _ in range(len(nums))]

        return self.helper(len(nums)-1,s1,dp,nums)
    
    def helper(self,ind,target,dp,nums):

        if ind==0:
            if target==0 and nums[0]==0:
                return 2
            if target==0:
                return 1
            if target==nums[0]:
                return 1
            return 0
        
        if dp[ind][target]!=-1:
            return dp[ind][target]
        
        nonPick=self.helper(ind-1,target,dp,nums)
        pick=self.helper(ind-1,target-nums[ind],dp,nums) if target>=nums[ind] else 0

        dp[ind][target]=pick+nonPick
        return dp[ind][target]
        