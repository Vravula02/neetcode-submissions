class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count=0
        visited=set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if (row,col) not in visited and grid[row][col]=="1":
                    count+=1
                    self.dfs(row,col,grid,visited)
        return count

    def dfs(self,row,col,grid,visited):

        visited.add((row,col))

        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            i,j=dr+row,dc+col

            if (i,j) not in visited and self.isValid(i,j,grid) and grid[i][j]=="1":
                self.dfs(i,j,grid,visited)
    
    def isValid(self,i,j,grid):

        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return False
        return True
        