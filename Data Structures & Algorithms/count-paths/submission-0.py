class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp=[[-1]*(n) for _ in range(m)]

        return self.helper(m-1,n-1,dp,m,n)
    
    def helper(self,row,col,dp,m,n):

        if row==0 or col==0:
            return 1
        
        if dp[row][col]!=-1:
            return dp[row][col]
        
        down=self.helper(row-1,col,dp,m,n)
        right=self.helper(row,col-1,dp,m,n)

        dp[row][col]=down+right

        return dp[row][col]
        