class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        mpp1=[0]*26
        mpp2=[0]*26

        for i in range(len(s1)):
            mpp1[ord(s1[i])-ord('a')]+=1
            mpp2[ord(s2[i])-ord('a')]+=1
        
        matches=0
        for i in range(26):
            if mpp1[i]==mpp2[i]:
                matches+=1
        
        left=0
        for i in range(len(s1),len(s2)):

            if matches==26:
                return True
            
            rightInd=ord(s2[i])-ord('a')

            mpp2[rightInd]+=1

            if mpp2[rightInd]==mpp1[rightInd]:
                matches+=1
            elif mpp2[rightInd]-1==mpp1[rightInd]:
                matches-=1
            
            leftInd=ord(s2[left])-ord('a')

            if mpp2[leftInd]==mpp1[leftInd]:
                matches-=1
            elif mpp2[leftInd]-1==mpp1[leftInd]:
                matches+=1
            mpp2[leftInd]-=1
            left+=1
        return matches==26




        