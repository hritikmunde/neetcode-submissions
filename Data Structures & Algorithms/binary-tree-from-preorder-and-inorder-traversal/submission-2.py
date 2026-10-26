# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        idx = {val: index for index, val in enumerate(inorder)}
        pre = 0
        def build(lo, hi):
            nonlocal pre
            if lo > hi:
                return None
            root_val = preorder[pre]
            pre += 1
            node = TreeNode(root_val)
            mid = idx[root_val]
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node
        return build(0, len(inorder) - 1)

