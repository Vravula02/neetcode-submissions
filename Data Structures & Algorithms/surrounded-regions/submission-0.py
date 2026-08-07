class Solution:
    def solve(self, board: List[List[str]]) -> None:

        visited=set()
        rows=len(board)
        cols=len(board[0])

        for r in range(rows):
            
            if board[r][0]=="O":
                self.dfs(r,0,visited,board)
            if board[r][cols-1]=="O":
                self.dfs(r,cols-1,visited,board)
        
        for c in range(cols):
            if board[0][c]=="O":
                self.dfs(0,c,visited,board)
            if board[rows-1][c]=="O":
                self.dfs(rows-1,c,visited,board)
               
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=="#":
                    board[row][col]="O"
                
                elif board[row][col]=="O":
                    board[row][col]="X"
        

        
    def dfs(self,row,col,visited,board):

        visited.add((row,col))
        board[row][col]="#"

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:

            i,j=row+dr,col+dc

            if (i,j) not in visited and self.isValid(i,j,board) and board[i][j]=="O":
                self.dfs(i,j,visited,board)

    def isValid(self,row,col,board):

        if row<0 or col<0 or row>=len(board) or col>=len(board[0]):
            return False
        return True