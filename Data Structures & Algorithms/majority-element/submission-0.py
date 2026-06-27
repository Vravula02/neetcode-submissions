class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count=0
        ele=None
        
        for num in nums:

            if ele==num:
                count+=1
            else:
                if count==0:
                    ele=num
                    count=1
                else:
                    count-=1
        return ele

        