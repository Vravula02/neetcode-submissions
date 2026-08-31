class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res=0

        charSet=set()
        left=0

        for right in range(len(s)):

            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            res=max(res,len(charSet))
        return res