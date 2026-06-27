class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        tool={")":"(","]":"[","}":"{"}

        for i in s:
            if i in tool:
                if len(stack)!=0 and tool[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if stack==[]:
            return True
        return False

        