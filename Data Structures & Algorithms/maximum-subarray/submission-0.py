class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans=float("-inf")
        temp=0

        for num in nums:

            temp+=num
            ans=max(ans,temp)

            if temp<0:
                temp=0
        return ans

        