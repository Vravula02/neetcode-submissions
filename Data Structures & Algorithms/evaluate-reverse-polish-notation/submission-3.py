class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                if len(stack)>=2:
                    val1=stack.pop()
                    val2=stack.pop()

                    op=tokens[i]

                    if op=="+":
                        stack.append(val1+val2)
                    elif op=="-":
                        stack.append(val2-val1)
                    elif op=="*":
                        stack.append(val1*val2)
                    elif op=="/":
                        stack.append(int(val2/val1))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
        