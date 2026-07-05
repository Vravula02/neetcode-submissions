class Solution:
    def jump(self, nums: List[int]) -> int:

        maxReach=0
        jump=0
        currentEnd=0

        for i in range(len(nums)-1):
            maxReach=max(maxReach,i+nums[i])

            if i==currentEnd:
                currentEnd=maxReach
                jump+=1
        return jump
        