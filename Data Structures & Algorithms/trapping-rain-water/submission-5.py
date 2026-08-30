class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        stack=[]
        res=0

        for i in range(len(height)):

            while stack and height[i]>=height[stack[-1]]:
                current=height[stack.pop()]

                if stack:
                    res+=(min(height[i],height[stack[-1]])-current)*(i-stack[-1]-1)
            stack.append(i)

        return res


