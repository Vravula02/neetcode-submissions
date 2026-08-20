class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1=len(word1)
        n2=len(word2)

        dp=[[-1]*(n2+1) for _ in range(n1+1)]

        return self.helper(0,0,word1,word2,dp)

    
    def helper(self,i,j,word1,word2,dp):

        if i==len(word1):
            return len(word2)-j
        if j==len(word2):
            return len(word1)-i
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if word1[i]==word2[j]:
            dp[i][j]=self.helper(i+1,j+1,word1,word2,dp)
        else:
            insert=1+self.helper(i,j+1,word1,word2,dp)
            delete=1+self.helper(i+1,j,word1,word2,dp)
            replace=1+self.helper(i+1,j+1,word1,word2,dp)

            dp[i][j]=min(insert,(min(delete,replace)))
        return dp[i][j]
