class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        pairs=[]

        for i in range(len(position)):
            pairs.append([speed[i],position[i]])
        
        pairs.sort(key=lambda x:x[1], reverse=True)

        stack=[]

        for pair in pairs:
            timeToFinish=(target-pair[1])/pair[0]
            stack.append(timeToFinish)

            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)