class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        row,col=len(matrix),len(matrix[0])

        dp=[[-1]*(col) for _ in range(row)]

        for r in range(row):
            for c in range(col):
                self.dfs(r,c,-1,matrix,dp)
        
        maxi=1

        for r in range(row):
            for c in range(col):
                maxi=max(maxi,dp[r][c])
        return maxi
    
    def dfs(self,r,c,prevVal,grid,dp):

        if not self.isValid(r,c,prevVal,grid):
            return 0
        
        if dp[r][c]!=-1:
            return dp[r][c]
        
        res=1

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            i,j=r+dr,c+dc
            res=max(res,1+self.dfs(i,j,grid[r][c],grid,dp))
        
        dp[r][c]=res
        return dp[r][c]

    def isValid(self,r,c,prevVal,grid):

        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or prevVal>=grid[r][c]:
            return False
        return True