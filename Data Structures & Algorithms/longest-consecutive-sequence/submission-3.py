class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0


        nums=set(nums)
        ans=1
        length=1

        for num in nums:
            if num-1 not in nums:
                length=1

                while num+length in nums:
                    length+=1
                ans=max(ans,length)
        return max(ans,length)
