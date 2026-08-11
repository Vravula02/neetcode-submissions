class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        nse=self.nse(heights)
        pse=self.pse(heights)

        ans=0

        for i in range(len(heights)):

            area=(nse[i]-pse[i]-1)*heights[i]
            ans=max(area,ans)
        return ans


    def nse(self,heights):

        n=len(heights)
        nse=[n]*n

        stack=[]

        for i in range(n-1,-1,-1):

            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            if stack:
                nse[i]=stack[-1]
            stack.append(i)
        return nse

    def pse(self,heights):

        n=len(heights)
        pse=[-1]*n

        stack=[]

        for i in range(n):

            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            if stack:
                pse[i]=stack[-1]
            stack.append(i)
        
        return pse
