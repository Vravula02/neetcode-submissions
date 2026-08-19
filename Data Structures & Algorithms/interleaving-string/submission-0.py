class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)

        if n1+n2!=n3:
            return False
        
        dp=[[False]*(n2+1) for _ in range(n1+1)]
        dp[n1][n2]=True

        for i in range(n1,-1,-1):
            for j in range(n2,-1,-1):

                if i<n1 and s3[i+j]==s1[i] and dp[i+1][j]==True:
                    dp[i][j]=True
                if j<n2 and s3[i+j]==s2[j] and dp[i][j+1]==True:
                    dp[i][j]=True
                
        return dp[0][0]
