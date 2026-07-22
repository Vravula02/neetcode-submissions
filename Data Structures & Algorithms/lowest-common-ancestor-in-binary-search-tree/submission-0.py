# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        if not root:
            return root
        
        leftTree=self.lowestCommonAncestor(root.left,p,q)
        rightTree=self.lowestCommonAncestor(root.right,p,q)

        if root.val>p.val and root.val>q.val:
            return leftTree
        
        if root.val<p.val and root.val<q.val:
            return rightTree
        
        else:
            return root
        
        
        



