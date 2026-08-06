class Solution:
    def reverse(self, x: int) -> int:

        mini=-(2**31)
        maxi=(2**31)-1

        res=0
        neg=0
        if x<0:
            neg=1
            x=x*-1


        while x:

            digit=x%10

            if res>(maxi//10) or (res==maxi and digit>(maxi%10)):
                return 0

            res=(res*10)+digit
            x=x//10

        return res if neg==0 else -res
        