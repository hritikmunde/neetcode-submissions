# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        subRoot_inorder = self.inorder(subRoot)
        root_inorder = self.inorder(root)
        if subRoot_inorder == root_inorder:
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def inorder(self, root):
        if root is None:
            return []
        return [root.val] + self.inorder(root.left) + self.inorder(root.right)
