class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        if nums==[]:
            return 0
        
        nums=[1]+nums+[1]
        dp=[[-1]*len(nums) for _ in range(len(nums))]

        return self.helper(1,len(nums)-2,nums,dp)
    
    def helper(self,left,right,nums,dp):

        if left>right:
            return 0
        
        if dp[left][right]!=-1:
            return dp[left][right]
        
        dp[left][right]=0
        
        for i in range(left,right+1):

            coins=nums[left-1]*nums[i]*nums[right+1]
            coins+=(self.helper(left,i-1,nums,dp)+self.helper(i+1,right,nums,dp))
            dp[left][right]=max(dp[left][right],coins)
        
        return dp[left][right]



        


