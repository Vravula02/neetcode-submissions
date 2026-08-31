class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n=len(s)
        maxFreq=0
        freq={}
        res=1
        left=0

        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            maxFreq=max(maxFreq,freq[s[right]])

            while (right-left+1)-maxFreq>k:
                freq[s[left]]-=1
                left+=1
            res=max(res,(right-left+1))
        return res

                