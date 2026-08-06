class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n==0:
            return []
        
        res=[]
        self.helper(0,0,"",res,n)
        return res
        
    
    def helper(self,left,right,current,res,n):

        if left==right==n:
            res.append(current)
            return
        
        if left<n:
            self.helper(left+1,right,current+"(",res,n)
        
        if left>right:
            return self.helper(left,right+1,current+")",res,n)
        
        
