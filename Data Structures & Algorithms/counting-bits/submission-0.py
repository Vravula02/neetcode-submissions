class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]

        for num in range(n+1):
            ans.append(self.countOnes(num))
        
        return ans

    def countOnes(self,n):

        mask=1
        count=0

        for _ in range(32):
            count+=(n&mask)
            n>>=1
        return count

        