# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, -math.inf, root.val) and self.dfs(root.right, root.val, math.inf)

    def dfs(self, root, left_bound, right_bound):
        if not root:
            return True
        if left_bound < root.val < right_bound:
            return self.dfs(root.left, left_bound, root.val) and self.dfs(root.right, root.val, right_bound)
        else:
            return False