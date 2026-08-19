class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2==1:
            return False
        
        target=int(sum(nums)/2)

        dp=[[-1 for _ in range(target+1)] for _ in range(len(nums)+1)]

        return self.helper(len(nums)-1,target,nums,dp)

    
    def helper(self,ind,target,nums,dp):

        if target==0:
            return True

        if ind==0:
            return target==nums[0]
        
        if dp[ind][target]!=-1:
            return dp[ind][target]
        
        nonTake=self.helper(ind-1,target,nums,dp)
        take=self.helper(ind-1,target-nums[ind],nums,dp) if nums[ind]<=target else False

        dp[ind][target]=(take or nonTake)
        return dp[ind][target]
        



        