class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []
            
        pac=set()
        atl=set()

        for row in range(len(heights)):
            self.dfs(row,0,-1,heights,pac)
            self.dfs(row,len(heights[0])-1,-1,heights,atl)
        
        for col in range(len(heights[0])):
            self.dfs(0,col,-1,heights,pac)
            self.dfs(len(heights)-1,col,-1,heights,atl)
        
        res=[]

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row,col) in pac and (row,col) in atl:
                    res.append([row,col])
        return res
        
    def dfs(self,row,col,prevHeight,heights,visited):

        if row<0 or col<0 or row>=len(heights) or col>=len(heights[0]) or prevHeight>heights[row][col]:
            return
        
        visited.add((row,col))

        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            i,j=row+dr,col+dc

            if (i,j) not in visited:
                self.dfs(i,j,heights[row][col],heights,visited)
        