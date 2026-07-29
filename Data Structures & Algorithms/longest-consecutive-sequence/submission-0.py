class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        ans=1
        temp=1

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue 
                
            if nums[i-1]+1==nums[i]:
                temp+=1
            else:
                ans=max(ans,temp)
                temp=1
        return max(ans,temp)
        