class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.backtracking(i,j,0,board,word):
                        return True
        return False
    

    def backtracking(self,row,col,k,board,word):

        if k==len(word):
            return True
        
        if row<0 or col<0 or row>=len(board) or col>=len(board[0]) or board[row][col]!=word[k]:
            return False
        

        temp=board[row][col]
        board[row][col]="#"

        ans=(self.backtracking(row+1,col,k+1,board,word) or self.backtracking(row-1,col,k+1,board,word) or self.backtracking(row,col+1,k+1,board,word) or self.backtracking(row,col-1,k+1,board,word))

        board[row][col]=temp

        return ans

        