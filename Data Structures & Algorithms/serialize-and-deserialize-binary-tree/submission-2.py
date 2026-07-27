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

        dq=collections.deque()
        dq.append(root)
        res=[]

        while dq:          

            node=dq.popleft()
            if node:
                res.append(str(node.val))
            else:
                res.append('#')
                continue

            dq.append(node.left)
            dq.append(node.right)
        
        return ",".join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data=="":
            return None

        vals=data.split(',')
        
        root=TreeNode(int(vals[0]))
        dq=collections.deque([root])
        ind=1

        while dq and ind<len(vals):
            
            node=dq.popleft()

            if vals[ind]!='#':
                node.left=TreeNode(int(vals[ind]))
                dq.append(node.left)
            ind+=1

            if vals[ind]!='#':
                node.right=TreeNode(int(vals[ind]))
                dq.append(node.right)
            ind+=1
        return root

        


       