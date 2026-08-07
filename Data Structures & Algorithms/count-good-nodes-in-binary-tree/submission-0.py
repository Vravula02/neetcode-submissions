# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count=0
        maxVal=float('-inf')
        dq=collections.deque([(root,maxVal)])

        while dq:

            node,maxVal=dq.popleft()

            if node.val>=maxVal:
                count+=1
                maxVal=node.val

            if node.left:
                dq.append((node.left,maxVal))
            if node.right:
                dq.append((node.right,maxVal))
        
        return count