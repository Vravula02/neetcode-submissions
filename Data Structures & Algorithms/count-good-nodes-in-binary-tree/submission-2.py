# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count=0
        maxi=float('-inf')
        dq=collections.deque([(root,maxi)])

        while dq:


            node,maxi=dq.popleft()

            if node.val>=maxi:
                count+=1
                maxi=node.val

            if node.left:
                dq.append((node.left,maxi))
            if node.right:
                dq.append((node.right,maxi))
        return count
            