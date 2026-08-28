class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c]!=".":
                    if board[r][c] in rows[r]:
                        return False
                    rows[r].add(board[r][c])
                
                    if board[r][c] in cols[c]:
                        return False
                    cols[c].add(board[r][c])

                    box=3*(r//3)+(c//3)
                    if board[r][c] in boxes[box]:
                        return False
                    boxes[box].add(board[r][c])
        return True
       