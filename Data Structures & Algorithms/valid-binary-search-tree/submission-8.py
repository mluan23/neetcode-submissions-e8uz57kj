# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, -1001, 1001)

    def traverse(self, root, lower, upper):
        if not root:
            return True
        if not (root.val < upper and root.val > lower):
            return False
        # if root.val <= lower or root.val >= upper:
        #     return False
        return (self.traverse(root.left, lower, root.val) and self.traverse(root.right, root.val, upper))