class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res=[]
        self.helper(0,[],target,res,candidates)
        return res

    def helper(self,ind,current,target,res,candidates):

        if target==0:
            res.append(current[:])
            return
        
        if ind==len(candidates) or target<0:
            return
        
        
        current.append(candidates[ind])
        self.helper(ind+1,current,target-candidates[ind],res,candidates)
        current.pop()

        for i in range(ind+1,len(candidates)):
            if candidates[i]!=candidates[ind]:
                self.helper(i,current,target,res,candidates)
                break
