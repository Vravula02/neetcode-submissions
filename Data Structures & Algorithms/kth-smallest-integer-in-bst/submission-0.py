# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k=k

        return self.inorder(root,self.k)
    
    def inorder(self,node,k):

        if not node:
            return None
        
        left_result=self.inorder(node.left,k)
        if left_result is not None:
            return left_result

        self.k-=1
        if self.k==0:
            return node.val

        return self.inorder(node.right,k)

 



        