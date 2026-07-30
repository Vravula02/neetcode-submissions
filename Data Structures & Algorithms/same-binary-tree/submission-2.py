# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q:
            return False

        stack1=[p]
        stack2=[q]

        while stack1 and stack2:

            p=stack1.pop()
            q=stack2.pop()

            if not p and not q:
                continue
            
            if not p or not q:
                return False
            
            if p.val!=q.val:
                return False
            
            stack1.append(p.left)
            stack1.append(p.right)
            stack2.append(q.left)
            stack2.append(q.right)
        
        return stack1==stack2==[]

        