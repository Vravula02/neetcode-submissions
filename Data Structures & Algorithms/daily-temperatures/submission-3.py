class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        nge=self.nge(temperatures)

        res=[0]*len(temperatures)

        for i in range(len(temperatures)):
            if nge[i]==0:
                continue
            res[i]=nge[i]-i
        return res


    def nge(self,nums):

        res=[0]*len(nums)
        stack=[]

        for i in range(len(nums)-1,-1,-1):

            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            
            if stack:
                res[i]=stack[-1]
            stack.append(i)
        return res

        