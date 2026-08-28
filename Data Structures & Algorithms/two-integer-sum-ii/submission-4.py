class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        mpp={}

        for i in range(len(numbers)):

            if target-numbers[i] in mpp:
                return [1+mpp[target-numbers[i]],i+1]
            mpp[numbers[i]]=i
        
        