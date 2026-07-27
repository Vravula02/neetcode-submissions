class Solution:
    def mySqrt(self, x: int) -> int:

        if x==0 or x==1:
            return x
        
        low=0
        high=x//2

        while low<=high:

            mid=(low+high)//2

            if mid**2==x:
                return mid

            if mid**2>x:
                high=mid-1
            else:
                low=mid+1
        return high