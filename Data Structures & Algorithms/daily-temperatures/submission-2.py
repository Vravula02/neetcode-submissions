class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res=[0]*len(temperatures)
        nge=self.nge(temperatures)

        for i in range(len(temperatures)):
            if nge[i]==-1:
                continue
            res[i]=nge[i]-i
        return res

    def nge(self,nums):

        stack=[]
        nge=[-1]*len(nums)

        for i in range(len(nums)-1,-1,-1):

            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            
            if stack:
                nge[i]=stack[-1]
            stack.append(i)
        
        return nge
            
            



