class Solution:
    def trap(self, height: List[int]) -> int:
        
        left=0
        right=len(height)-1
        leftMax=0
        rightMax=height[-1]

        ans=0

        while left<right:

            if height[left]<=height[right]:

                if leftMax>height[left]:
                    ans+=(leftMax-height[left])
                else:
                    leftMax=height[left]
                left+=1
            else:

                if rightMax>height[right]:
                    ans+=(rightMax-height[right])
                else:
                    rightMax=height[right]
                right-=1
        return ans
