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
    
        st1=[p]
        st2=[q]

        while st1 and st2:

            p=st1.pop()
            q=st2.pop()

            if not p and not q:
                continue
            if not p or not q:
                return False
            
            if p.val!=q.val:
                return False
            
            st1.append(p.left)
            st1.append(p.right)
            st2.append(q.left)
            st2.append(q.right)
        
        return st1==st2==[]

