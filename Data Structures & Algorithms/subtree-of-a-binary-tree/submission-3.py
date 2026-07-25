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
        
        if self.sameTree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        
        
        
        
    def sameTree(self,p,q):

        st1,st2=[p],[q]

        while st1 and st2:

            node1,node2=st1.pop(),st2.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            
            if node1.val!=node2.val:
                return False
            
            st1.append(node1.left)
            st1.append(node1.right)
            st2.append(node2.left)
            st2.append(node2.right)

        return st1==st2==[]


