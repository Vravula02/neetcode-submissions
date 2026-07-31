# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.mpp={val:ind for ind,val in enumerate(inorder)}

        return self.construct(0,len(inorder)-1,0,len(preorder)-1,inorder,preorder)
    
    def construct(self,inStart,inEnd,preStart,preEnd,inorder,preorder):

        if inStart>inEnd or preStart>preEnd:
            return
        
        rootVal=preorder[preStart]
        root=TreeNode(rootVal)
        rootIndInorder=self.mpp[rootVal]
        leftLen=rootIndInorder-inStart

        root.left=self.construct(inStart,rootIndInorder-1,preStart+1,preStart+leftLen,inorder,preorder)

        root.right=self.construct(rootIndInorder+1,inEnd,preStart+leftLen+1,preEnd,inorder,preorder)

        return root
