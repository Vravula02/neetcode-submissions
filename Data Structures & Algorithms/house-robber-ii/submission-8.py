class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]


        nums1=nums[1:]
        nums2=nums[:-1]

        dp1=[-1]*len(nums1)
        dp2=[-1]*len(nums2)

        return max(self.helper(len(nums1)-1,nums1,dp1),self.helper(len(nums2)-1,nums2,dp2))

    
    def helper(self,ind,nums,dp):

        if ind==0:
            return nums[0]
        if ind==1:
            return max(nums[0],nums[1])
        
        if dp[ind]!=-1:
            return dp[ind]
        
        notTaken=self.helper(ind-1,nums,dp)
        taken=self.helper(ind-2,nums,dp)+nums[ind] if ind>=2 else 0

        dp[ind]=max(taken,notTaken)
        return dp[ind]
        