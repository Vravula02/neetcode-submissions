class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n=len(heights)
        stack=[]
        ans=0

        for i in range(n):

            while stack and heights[stack[-1]]>=heights[i]:
                current=stack.pop()
                nse=i

                if stack:
                    pse=stack[-1]
                else:
                    pse=-1
                
                area=(nse-pse-1)*heights[current]

                ans=max(area,ans)
            stack.append(i)
        
        while stack:
            nse=n

            current=stack.pop()
            pse=stack[-1] if stack else -1

            area=(nse-pse-1)*heights[current]
            ans=max(area,ans)
        
        return ans