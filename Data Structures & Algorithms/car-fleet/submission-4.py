class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars=[]

        for i in range(len(speed)):
            cars.append([speed[i],position[i]])
        
        cars.sort(key=lambda x:x[1],reverse=True)
        stack=[]

        for i in range(len(speed)):

            timeTaken=(target-cars[i][1])/cars[i][0]

            while not stack or stack[-1]<timeTaken:
                stack.append(timeTaken)
            
        return len(stack)

