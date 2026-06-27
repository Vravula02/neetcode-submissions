class Solution:
    def hammingWeight(self, n: int) -> int:

        mask=1
        count=0

        for _ in range(32):
            count+=(n&mask)
            n=n>>1
        return count
        