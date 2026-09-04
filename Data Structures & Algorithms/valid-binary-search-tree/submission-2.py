# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        return self.helper(root,float('inf'),float('-inf'))
    

    def helper(self,root,maxVal,minVal):

        if not root:
            return True

        if root.val>=maxVal or root.val<=minVal:
            return False
        
        left=self.helper(root.left,root.val,minVal)
        right=self.helper(root.right,maxVal,root.val)

        return left and right

        
        

        

        