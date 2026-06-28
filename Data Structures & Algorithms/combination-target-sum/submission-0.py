class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans=[]
        self.helper(0,nums,[],target,ans)
        return ans
    
    def helper(self,idx,nums,current,target,ans):

        if target==0:
            ans.append(current[:])
            return 

        if target<0 or idx==len(nums):
            return
        

        current.append(nums[idx])
        self.helper(idx,nums,current,target-nums[idx],ans)

        current.pop()
        self.helper(idx+1,nums,current,target,ans)
        