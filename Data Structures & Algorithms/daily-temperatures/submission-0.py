class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        nge=self.findNge(temperatures)
        ans=[0]*len(temperatures)

        for i in range(len(temperatures)):
            ans[i]=nge[i]-i if nge[i]!=0 else 0
        
        return ans
    
    def findNge(self,temperatures):

        n=len(temperatures)
        nge=[0]*n

        stack=[]

        for i in range(n-1,-1,-1):

            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            
            if stack:
                nge[i]=stack[-1]
            stack.append(i)
        
        return nge