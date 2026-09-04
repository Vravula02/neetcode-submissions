# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""
        
        res=[]

        dq=collections.deque([root])

        while dq:

            node=dq.popleft()

            if node:
                res.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                res.append("#")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data=="":
            return None
        
        data=data.split(',')
        
        root=TreeNode(int(data[0]))
        ind=1
        dq=collections.deque([root])

        while dq:

            node=dq.popleft()

            if data[ind]!="#":
                node.left=TreeNode(int(data[ind]))
                dq.append(node.left)
            ind+=1

            if data[ind]!="#":
                node.right=TreeNode(int(data[ind]))
                dq.append(node.right)
            ind+=1
        
        return root

        

