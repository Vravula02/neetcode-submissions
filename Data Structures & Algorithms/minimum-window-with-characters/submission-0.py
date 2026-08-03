class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        minLen=float('inf')
        start=-1

        for i in range(len(s)):

            mpp=[0]*256

            for ch in t:
                mpp[ord(ch)]+=1
            count=0

            for j in range(i,len(s)):

                if mpp[ord(s[j])]>0:
                    count+=1
                mpp[ord(s[j])]-=1

                if count==len(t):
                    if j-i+1<minLen:
                        minLen=j-i+1
                        start=i
                        break
        return s[start:start+minLen] if start!=-1 else ""


            
