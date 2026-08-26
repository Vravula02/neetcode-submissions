class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res=[]
        self.generate(0,[],nums,res)
        return res



    def generate(self,ind,current,nums,res):

        if ind==len(nums):
            res.append(current[:])
            return
        
        current.append(nums[ind])
        self.generate(ind+1,current,nums,res)

        current.pop()
        self.generate(ind+1,current,nums,res)