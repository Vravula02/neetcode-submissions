class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res=[]
        self.backtracking(0,[],res,s)
        return res
        
    def backtracking(self,ind,current,res,s):

        if ind==len(s):
            res.append(current[:])
            return
        
        for end in range(ind+1,len(s)+1):
            if self.isPallindrome(s[ind:end]):
                current.append(s[ind:end])
                self.backtracking(end,current,res,s)
                current.pop()
        
    
    def isPallindrome(self,s):
        return s==s[::-1]