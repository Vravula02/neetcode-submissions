class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if not heights:
            return 0
        
        area=0

        pse=self.pse(heights)
        nse=self.nse(heights)

        for i in range(len(heights)):

            length=(nse[i]-pse[i]-1)
            height=heights[i]
            area=max(area,length*height)
        return area

    
    def pse(self,nums):

        n=len(nums)
        res=[-1]*(n)

        stack=[]

        for i in range(n):

            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            
            if stack:
                res[i]=stack[-1]
            stack.append(i)
        return res
    
    def nse(self,nums):

        n=len(nums)
        res=[n]*n
        stack=[]

        for i in range(n-1,-1,-1):

            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            
            if stack:
                res[i]=stack[-1]
            stack.append(i)
        return res


        