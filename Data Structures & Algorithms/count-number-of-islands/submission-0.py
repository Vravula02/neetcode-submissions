class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count=0

        visited=set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if (i,j) not in visited and grid[i][j]=="1":
                    visited.add((i,j))
                    count+=1
                    self.bfs(i,j,grid,visited)
        return count
    
    def bfs(self,i,j,grid,visited):

        dq=collections.deque([(i,j)])

        while dq:

            for _ in range(len(dq)):
                
                row,col=dq.popleft()

                for dr,dc in [(0,1),(-1,0),(1,0),(0,-1)]:
                    checkRow=row+dr
                    checkCol=col+dc

                    if self.isValid(checkRow,checkCol,grid) and grid[checkRow][checkCol]=="1":
                        if (checkRow,checkCol) not in visited:
                            visited.add((checkRow,checkCol))
                            dq.append((checkRow,checkCol))
    
    def isValid(self,i,j,grid):

        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return False
        return True
        



        