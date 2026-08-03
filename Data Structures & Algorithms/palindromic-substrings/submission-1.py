class Solution:
    def countSubstrings(self, s: str) -> int:

        self.ans=0

        for i in range(len(s)):
            self.expand(i,i,s)
            self.expand(i,i+1,s)
        return self.ans
        
    def expand(self,left,right,s):

        while left>=0 and right<len(s) and s[left]==s[right]:
            self.ans+=1
            left-=1
            right+=1
    
