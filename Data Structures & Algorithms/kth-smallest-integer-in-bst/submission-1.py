# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        vals=[]
        self.inorder(root,vals)

        return vals[k-1]

    def inorder(self,root,vals):

        if not root:
            return 
        
        self.inorder(root.left,vals)
        vals.append(root.val)
        self.inorder(root.right,vals)
        