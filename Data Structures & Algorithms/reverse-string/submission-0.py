class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if len(s)==0 or len(s)==1:
            return s
        
        left=0
        right=len(s)-1

        while left<right:
            s[right],s[left]=s[left],s[right]
            left+=1
            right-=1
        
        return s
        