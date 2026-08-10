class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        mpp1=[0]*26
        mpp2=[0]*26
        count=0

        for i in range(len(s1)):
            mpp1[ord(s1[i])-ord('a')]+=1
            mpp2[ord(s2[i])-ord('a')]+=1
        
        for i in range(26):
            if mpp1[i]==mpp2[i]:
                count+=1

        left=0
        for right in range(len(s1),len(s2)):

            if count==26:
                return True
            
            rightIdx=ord(s2[right])-ord('a')

            mpp2[rightIdx]+=1

            if mpp2[rightIdx]==mpp1[rightIdx]:
                count+=1
            elif mpp2[rightIdx]==mpp1[rightIdx]+1:
                count-=1

            leftIdx=ord(s2[left])-ord('a')
            mpp2[leftIdx]-=1

            if mpp2[leftIdx]==mpp1[leftIdx]:
                count+=1
            elif mpp1[leftIdx]-1==mpp2[leftIdx]:
                count-=1
            
            left+=1
        return count==26