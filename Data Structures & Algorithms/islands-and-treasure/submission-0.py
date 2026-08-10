class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        dq=collections.deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    dq.append((row,col,0))
            
        inf=2147483647

        while dq:

            for _ in range(len(dq)):
                row,col,dist=dq.popleft()

                for dr,dc in [(1,0),(-1,0),(0,-1),(0,1)]:
                    i,j=row+dr,col+dc

                    if self.isValid(i,j,grid) and grid[i][j]==inf:
                        grid[i][j]=dist+1
                        dq.append((i,j,dist+1))
        
    def isValid(self,row,col,grid):

        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):
            return False
        return True
    