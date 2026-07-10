class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j]==".":
                    continue

                num=board[i][j]

                for row in range(9):
                    if row!=i and board[row][j]==num:
                        return False
                
                for col in range(9):
                    if col!=j and board[i][col]==num:
                        return False
                
                dr=(i//3)*3
                dc=(j//3)*3

                for row in range(dr,dr+3):
                    for col in range(dc,dc+3):

                        if row!=i and col!=j and board[row][col]==num:
                            return False
        return True