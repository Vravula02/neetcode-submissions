# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        return self.dfs(root,float('-inf'))
    
    def dfs(self,root,maxi):

        if not root:
            return 0

        res=1 if root.val>=maxi else 0

        maxi=max(maxi,root.val)
        res+=self.dfs(root.left,maxi)
        res+=self.dfs(root.right,maxi)

        return res
