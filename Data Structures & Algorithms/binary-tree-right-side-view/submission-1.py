# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque
        if not root:
            return []
        dq=deque([(root,0,0)])

        mpp={}

        while dq:
            for _ in range(len(dq)):

                node,row,col=dq.popleft()

                if node.left:
                    dq.append((node.left,row+1,col-1))
                if node.right:
                    dq.append((node.right,row+1,col+1))

                mpp[row]=node.val
        
        ans=[val for key,val in mpp.items()]
        return ans