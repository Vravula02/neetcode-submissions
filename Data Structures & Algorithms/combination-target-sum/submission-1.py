class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]
        self.helper(0,[],target,res,nums)
        return res

    def helper(self,ind,current,target,res,nums):

        if target==0:
            res.append(current[:])
            return
        
        if target<0 or ind==len(nums):
            return
        
        current.append(nums[ind])
        self.helper(ind,current,target-nums[ind],res,nums) 

        current.pop()
        self.helper(ind+1,current,target,res,nums)
        


        