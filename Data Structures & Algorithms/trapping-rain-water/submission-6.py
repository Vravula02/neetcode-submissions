class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left=0
        right=len(height)-1
        leftMax=0
        rightMax=height[-1]

        res=0

        while left<right:

            if height[left]<=height[right]:

                if leftMax>height[left]:
                    res+=(leftMax-height[left])
                else:
                    leftMax=height[left]
                left+=1
            else:

                if rightMax>height[right]:
                    res+=(rightMax-height[right])
                else:
                    rightMax=height[right]
                right-=1
        return res