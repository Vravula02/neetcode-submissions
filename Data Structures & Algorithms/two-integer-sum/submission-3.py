class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mpp={}

        for i in range(len(nums)):
            if target-nums[i] in mpp:
                return [mpp[target-nums[i]],i]
            mpp[nums[i]]=i
        