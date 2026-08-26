class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans=float('-inf')
        preffix=1
        suffix=1

        for i in range(len(nums)):

            if preffix==0:
                preffix=1
            if suffix==0:
                suffix=1
            
            preffix*=nums[i]
            suffix*=nums[len(nums)-1-i]

            ans=max(ans,max(preffix,suffix))
        return ans



       