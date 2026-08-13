class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res=[]
        board=[["." for _ in range(n)] for _ in range(n)]
        self.placeQueen(0,0,board,res)
        return res
    
    def placeQueen(self,row,col,board,res):

        if col==len(board[0]):
            res.append(["".join(row) for row in board])
            return 

        for row in range(len(board)):
            if self.isValid(row,col,board):
                board[row][col]="Q"
                self.placeQueen(row,col+1,board,res)
                board[row][col]="."
            

    def isValid(self,row,col,board):

        for i in range(col):
            if board[row][i]=="Q":
                return False
        
        r=row-1
        c=col-1
        while r>=0 and c>=0:
            if board[r][c]=="Q":
                return False
            r-=1
            c-=1
        
        r=row+1
        c=col-1

        while c>=0 and r<len(board):
            if board[r][c]=="Q":
                return False
            c-=1
            r+=1
        return True



        