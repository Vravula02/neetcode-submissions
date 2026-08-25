class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping={')':'(',']':'[','}':'{'}

        stack=[]

        for ch in s:

            if ch in mapping:
                if not stack:
                    return False
                if stack.pop()!=mapping[ch]:
                    return False
            else:
                stack.append(ch)
        return stack==[]