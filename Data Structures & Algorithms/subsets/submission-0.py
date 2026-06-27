class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        self.generate(0,nums,[],ans)
        return ans
    
    def generate(self,idx,nums,current,ans):

        if idx==len(nums):
            ans.append(current[:])
            return
        
        current.append(nums[idx])
        self.generate(idx+1,nums,current,ans)

        current.pop()
        self.generate(idx+1,nums,current,ans)