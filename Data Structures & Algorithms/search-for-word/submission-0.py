class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.helper(i,j,board,0,word):
                        return True
        return False
    
    def helper(self,i,j,board,k,word):

        if k==len(word):
            return True

        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[k]:
            return False

        
        temp=board[i][j]
        board[i][j]='#'
        
        ans=(self.helper(i+1,j,board,k+1,word) or self.helper(i-1,j,board,k+1,word) or self.helper(i,j+1,board,k+1,word) or self.helper(i,j-1,board,k+1,word) )
        board[i][j]=temp

        return ans

        
        