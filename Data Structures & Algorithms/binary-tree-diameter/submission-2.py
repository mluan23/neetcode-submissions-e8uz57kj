# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # so the diameter is just the sum of 
        # the left and right subtree heights + 1 (for the parent)
        # so how do you find height?
        self.max_diam = 0
        # ok so this finds height
        def find_height(root):
            if root is None:
                return 0
            l = find_height(root.left)
            r = find_height(root.right)
            self.max_diam = max(self.max_diam, l + r)
            return 1 + max(l, r)
        find_height(root)
        return self.max_diam
            

    