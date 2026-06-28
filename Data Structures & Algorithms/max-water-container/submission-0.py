class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):

                ans=max(ans,(min(heights[i],heights[j])*(j-i)))
        return ans