class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low=0
        high=len(matrix)-1

        while low<=high:
            mid=(low+high)//2

            if matrix[mid][-1]<target:
                low=mid+1
            elif matrix[mid][0]>target:
                high=mid-1
            else:
                break
        
        if not low<=high:
            return False
        
        row=(low+high)//2
        
        left=0
        right=len(matrix[0])-1

        while left<=right:

            mid=(left+right)//2

            if target>matrix[row][mid]:
                left=mid+1
            elif target<matrix[row][mid]:
                right=mid-1
            else:
                return True
        return False
