class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            for col in range(9):
                if not self.isValid(row,col,board):
                    return False
        return True
                


    def isValid(self,row,col,board):

        if board[row][col]!=".":

            for r in range(9):
                if r==row:
                    continue
                if board[r][col]==board[row][col]:
                    return False
            
            for c in range(9):
                if c==col:
                    continue
                if board[row][c]==board[row][col]:
                    return False
            
            startRow=(row//3)*3
            startCol=(col//3)*3

            for r in range(startRow,startRow+3):
                for c in range(startCol,startCol+3):
                    if r==row and c==col:
                        continue
                    if board[r][c]==board[row][col]:
                        return False
        return True
        