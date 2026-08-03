class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        minLen=float('inf')
        start=-1
        count=0

        mpp=[0]*256

        for ch in t:
            mpp[ord(ch)]+=1
        
        left,right=0,0

        while right<len(s):

            if mpp[ord(s[right])]>0:
                count+=1
            mpp[ord(s[right])]-=1

            while count==len(t):

                if right-left<minLen:
                    minLen=right-left+1
                    start=left
                
                mpp[ord(s[left])]+=1

                if mpp[ord(s[left])]>0:
                    count-=1
                left+=1
            
            right+=1
        
        return s[start:start+minLen] if start!=-1 else ""