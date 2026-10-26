# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialised = []
        def dfs(root):
            if not root:
                serialised.append("N")
                return
            serialised.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(serialised)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        index = 0
        def dfs():
            nonlocal index
            val = vals[index]
            if val == "N":
                index += 1
                return None
            node = TreeNode(int(val))
            index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root
