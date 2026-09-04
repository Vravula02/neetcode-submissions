# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.mpp={val:ind for ind,val in enumerate(inorder)}

        return self.builder(0,len(inorder)-1,0,len(preorder)-1,inorder,preorder)
    
    def builder(self,inStart,inEnd,preStart,preEnd,inorder,preorder):

        if inStart>inEnd or preStart>preEnd:
            return 
        
        rootVal=preorder[preStart]
        root=TreeNode(rootVal)
        rootInd=self.mpp[rootVal]
        leftLen=rootInd-inStart

        root.left=self.builder(inStart,rootInd-1,preStart+1,preStart+leftLen,inorder,preorder)

        root.right=self.builder(rootInd+1,inEnd,preStart+leftLen+1,preEnd,inorder,preorder)

        return root
        