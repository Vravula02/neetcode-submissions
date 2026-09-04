# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        count=0
        dq=collections.deque([(root,float('-inf'))])

        while dq:

            node,maxVal=dq.popleft()

            if node.val>=maxVal:
                maxVal=node.val
                count+=1
            
            if node.left:
                dq.append((node.left,maxVal))
            if node.right:
                dq.append((node.right,maxVal))
        return count
        