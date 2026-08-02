class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m==0 or n==0:
            return 1
        
        dp=[[-1 for _ in range(n)]for _ in range(m)]

        return self.helper(m-1,n-1,m,n,dp)
    
    def helper(self,row,col,m,n,dp):

        if row==0 or col==0:
            dp[row][col]=1
            return dp[row][col]
        
        if dp[row][col]!=-1:
            return dp[row][col]
        
        top=self.helper(row-1,col,m,n,dp)
        left=self.helper(row,col-1,m,n,dp)

        dp[row][col]=left+top
        return dp[row][col]