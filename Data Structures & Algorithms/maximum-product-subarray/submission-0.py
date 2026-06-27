class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefix=1
        suffix=1
        prod=float("-inf")
        n=len(nums)

        for i in range(n):

            if prefix==0:
                prefix=1
            
            if suffix==0:
                suffix=1
            
            prefix*=nums[i]
            suffix*=nums[n-1-i]
            
            prod=max(prod,max(prefix,suffix))
        return prod