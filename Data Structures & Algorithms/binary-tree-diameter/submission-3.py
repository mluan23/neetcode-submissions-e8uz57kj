# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # to find this just take the sum of left and right
        # subtrees
        # get the maximum
        # we can get height for any given node for l and r
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return max(max(left_height + right_height, self.diameterOfBinaryTree(root.left)), self.diameterOfBinaryTree(root.right))

    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
