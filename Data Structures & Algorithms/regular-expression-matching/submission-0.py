class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp={}

        return self.helper(0,0,s,p,dp)

    def helper(self,i,j,s,p,dp):

        if i>=len(s) and j>=len(p):
            return True
        
        if i<len(s) and j>=len(p):
            return False
        
        if (i,j) in dp:
            return dp[(i,j)]

        match=i<len(s) and (s[i]==p[j] or p[j]==".")

        if j+1<len(p) and p[j+1]=="*":

            nonTake=self.helper(i,j+2,s,p,dp)
            take=match and self.helper(i+1,j,s,p,dp)

            dp[(i,j)]=take or nonTake
            return dp[(i,j)]
        
        if match:
            dp[(i,j)]=self.helper(i+1,j+1,s,p,dp)
            return dp[(i,j)]
        
        dp[(i,j)]=False
        return dp[(i,j)]
