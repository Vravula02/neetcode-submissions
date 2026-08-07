class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited=set()
        ans=0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col]==1:
                    ans=max(ans,self.dfs(row,col,visited,grid))
        return ans
        

    def dfs(self,row,col,visited,grid):

        visited.add((row,col))
        area=1

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:

            i,j=row+dr,col+dc

            if self.isValid(i,j,grid) and (i,j) not in visited and grid[i][j]==1:
                visited.add((i,j))
                area+=self.dfs(i,j,visited,grid)
        return area
    

    def isValid(self,row,col,grid):

        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):
            return False
        
        return True