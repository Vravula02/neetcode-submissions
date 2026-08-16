class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        visited=set()
        pq=[]

        heapq.heappush(pq,(grid[0][0],0,0))
        visited.add((0,0))

        n=len(grid)
        m=len(grid[0])

        while pq:

            maxi,r,c=heapq.heappop(pq)

            if r==n-1 and c==m-1:
                return maxi
            
            for dr,dc in [(0,-1),(0,1),(1,0),(-1,0)]:
                i=r+dr
                j=c+dc

                if self.isValid(i,j,grid) and (i,j) not in visited:
                    newMax=max(maxi,grid[i][j])
                    visited.add((i,j))
                    heapq.heappush(pq,(newMax,i,j))

        
    
    def isValid(self,r,c,grid):

        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
            return False
        return True