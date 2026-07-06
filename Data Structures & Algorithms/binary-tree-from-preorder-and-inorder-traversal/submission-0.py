# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.mpp={val:idx for idx,val in enumerate(inorder)}

        return self.builder(0,len(preorder)-1,0,len(inorder)-1,preorder,inorder)


    def builder(self,preStart,preEnd,inStart,inEnd,preorder,inorder):

        if preStart>preEnd or inStart>inEnd:
            return 
         
        rootVal=preorder[preStart]
        root=TreeNode(rootVal)
        rootInIdx=self.mpp[rootVal]
        leftLen=rootInIdx-inStart

        root.left=self.builder(preStart+1,preStart+leftLen,inStart,rootInIdx-1,preorder,inorder)
        root.right=self.builder(preStart+leftLen+1,preEnd,rootInIdx+1,inEnd,preorder,inorder)

        return root
