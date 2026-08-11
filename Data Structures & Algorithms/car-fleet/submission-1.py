class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        pairs=[]

        for i in range(len(position)):
            pairs.append([speed[i],position[i]])
        
        pairs.sort(key=lambda x:x[1])

        stack=[]

        for i in range(len(pairs)-1,-1,-1):
            timeToFinish=(target-pairs[i][1])/pairs[i][0]
            stack.append(timeToFinish)

            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)