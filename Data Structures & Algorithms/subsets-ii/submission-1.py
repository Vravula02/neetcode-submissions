class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        self.helper(0,[],nums,ans)
        return ans
    
    def helper(self,idx,current,nums,ans):

        if idx==len(nums):
            ans.append(current[:])
            return
        
        current.append(nums[idx])
        self.helper(idx+1,current,nums,ans)

        current.pop()

        for i in range(idx+1,len(nums)):
            if nums[i]!=nums[idx]:
                self.helper(i,current,nums,ans)
                return
        self.helper(len(nums),current,nums,ans)

        