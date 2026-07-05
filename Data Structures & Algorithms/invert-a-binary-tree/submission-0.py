# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        dq=collections.deque([root])
        
        while dq:
            for _ in range(len(dq)):
                node=dq.popleft()

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

                node.left,node.right=node.right,node.left
        return root