class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp=[[-1]*len(t) for _ in range(len(s))]
        return self.helper(0,0,s,t,dp)
    
    def helper(self,i,j,s,t,dp):

        if j==len(t):
            return 1
        if i==len(s):
            return 0
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if s[i]==t[j]:
            dp[i][j]=self.helper(i+1,j+1,s,t,dp)+self.helper(i+1,j,s,t,dp)
        else:
            dp[i][j]=self.helper(i+1,j,s,t,dp)
        return dp[i][j]
        