class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans=[]

        for i in range(len(nums)-2):

            if i>0 and nums[i-1]==nums[i]:
                continue
            
            left=i+1
            right=len(nums)-1

            while left<right:
                triSum=nums[i]+nums[left]+nums[right]

                if triSum>0:
                    right-=1
                elif triSum<0:
                    left+=1
                else:
                    ans.append([nums[i],nums[left],nums[right]])

                    while left<len(nums)-1 and nums[left]==nums[left+1]:
                        left+=1
                    
                    while right>i+1 and nums[right]==nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1
                    
        return ans


        