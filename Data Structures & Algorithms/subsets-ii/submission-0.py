class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res=[]
        self.helper(0,nums,[],res)
        return res

    def helper(self,ind,nums,current,res):
            res.append(current[::])
            
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                current.append(nums[i])

                self.helper(i+1,nums,current,res)
                current.pop()
                