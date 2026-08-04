class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num=""
        for i in range(len(digits)):
            num+=str(digits[i])

        num=str(int(num)+1)

        res=[0]*len(num)

        for i in range(len(num)):
            res[i]=int(num[i])
        return res

