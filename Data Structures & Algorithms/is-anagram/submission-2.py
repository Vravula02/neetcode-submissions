class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        visited=[0]*26

        for ch in s:
            visited[ord(ch)-ord('a')]+=1
        
        for ch in t:

            if visited[ord(ch)-ord('a')]<=0:
                return False
            visited[ord(ch)-ord('a')]-=1

        return sum(visited)==0
            
        