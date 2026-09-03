# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val==subRoot.val:
            if self.sameTree(root,subRoot):
                return True
        
        if self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot):
            return True
        return False

    

    def sameTree(self,p,q):

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