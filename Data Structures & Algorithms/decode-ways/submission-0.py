class Solution:
    def numDecodings(self, s: str) -> int:
        
        n=len(s)
        dp=[-1]*(n)

        return self.helper(0,s,dp)


    def helper(self,ind,s,dp):

        if ind==len(s):
            return 1
        if s[ind]=="0":
            return 0
        
        if dp[ind]!=-1:
            return dp[ind]
        
        oneDigit=self.helper(ind+1,s,dp)
        twoDigit=0

        if ind<len(s)-1:
            if s[ind]=="1" or (s[ind]=="2" and s[ind+1]<='6'):
                twoDigit=self.helper(ind+2,s,dp)
        dp[ind]=oneDigit+twoDigit
        return dp[ind]