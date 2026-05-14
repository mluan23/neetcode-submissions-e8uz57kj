# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we have to keep some sort of running maximum per side then
        # so we just keep the current max for the branch
        return self.dfs(root, root.val)
    def dfs(self, root, max_val):
        if not root:
            return 0
        if root.val < max_val:
            return self.dfs(root.left, max_val) + self.dfs(root.right, max_val)
        else:
            return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val) 