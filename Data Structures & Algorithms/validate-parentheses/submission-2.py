class Solution:
    def isValid(self, s: str) -> bool:

        mpp={')':'(','}':'{',']':'['}

        stack=[]

        for ch in s:

            if ch in mpp:
                if not stack:
                    return False
                elif mpp[ch]!=stack.pop():
                    return False
            else:
                stack.append(ch)
        return stack==[]
