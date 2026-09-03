# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        store={}

        dq=collections.deque([(root,0,0)])

        while dq:

            for _ in range(len(dq)):

                node,row,col=dq.popleft()

                store[row]=node.val

                if node.left:
                    dq.append((node.left,row+1,col-1))
                if node.right:
                    dq.append((node.right,row+1,col+1))
        return [val for val in store.values() ]

        
        