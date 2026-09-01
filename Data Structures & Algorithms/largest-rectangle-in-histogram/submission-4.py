class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if not heights:
            return 0
        
        area=0

        stack=[]

        for i in range(len(heights)):

            while stack and heights[stack[-1]]>=heights[i]:

                current=stack.pop()
                nse=i

                if stack:
                    pse=stack[-1]
                else:
                    pse=-1
                
                area=max((nse-pse-1)*(heights[current]),area)
            stack.append(i)
        
        while stack:
            current=stack.pop()
            nse=len(heights)
            pse=stack[-1] if stack else -1

            area=max((nse-pse-1)*(heights[current]),area)
        return area

        