class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans=[]
        nums.sort()

        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left=i+1
            right=len(nums)-1

            while left<right:

                sumVal=nums[i]+nums[right]+nums[left]

                if sumVal>0:
                    right-=1
                elif sumVal<0:
                    left+=1
                else:
                    ans.append([nums[i],nums[left],nums[right]])

                    while left<len(nums)-1:
                        if nums[left]!=nums[left+1]:
                            break
                        left+=1
                    
                    while right>i+1:
                        if nums[right]!=nums[right-1]:
                            break
                        right-=1
                    left+=1
                    right-=1
                        
        return ans
        