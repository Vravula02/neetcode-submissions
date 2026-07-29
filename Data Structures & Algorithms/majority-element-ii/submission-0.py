class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        num1,num2=None,None
        freq1,freq2=0,0

        for num in nums:

            if num==num1:
                freq1+=1
            elif num==num2:
                freq2+=1
            else:
                if freq1==0 and freq2==0:
                    freq1+=1
                    num1=num
                elif freq1==0:
                    freq1+=1
                    num1=num
                elif freq2==0:
                    freq2+=1
                    num2=num
                  
                else:
                    freq1-=1
                    freq2-=1
        freq1=0
        freq2=0

        for num in nums:
            if num==num1:
                freq1+=1
            elif num==num2:
                freq2+=1
            
        ans=[]
        if freq1>len(nums)//3:
            ans.append(num1)
        if freq2>len(nums)//3:
            ans.append(num2)

        return ans


        