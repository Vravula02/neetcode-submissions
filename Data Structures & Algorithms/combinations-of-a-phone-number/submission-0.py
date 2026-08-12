class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits=="":
            return []
        
        trace={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":       ["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        
        res=[]
        self.backtracking(0,digits,"",res,trace)
        return res

    def backtracking(self,ind,digits,current,res,trace):

        if ind==len(digits):
            res.append(current[::])
            return
        
        charRange=trace[digits[ind]]

        for ch in charRange:
            self.backtracking(ind+1,digits,current+ch,res,trace)

        