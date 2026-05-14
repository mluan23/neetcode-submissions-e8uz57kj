# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # so for this we have to track the max val/min val we
        # are allowed to go past
        # ok so for left - your initial val MUST be less than root val, and it can be any num smaller - correct
        # and for right - init val MUST be greater tahn root.val, and inf upper bound - loks fine
        return self.dfs(root.left, -math.inf, root.val) and self.dfs(root.right, root.val, math.inf)
    def dfs(self, root, lower_bound, upper_bound):
        # lower vs upper bound; you must greater than lower bound,
        # lt upper bound
        if not root:
            return True
        if not lower_bound < root.val < upper_bound:
            return False
        # now what should this be
        # if we take the left subtree, the new lower bound should still be negative inf right?
        # so we take the original lower bound still
        # but the upper bound becomes the actual root
        return self.dfs(root.left, lower_bound, root.val) and self.dfs(root.right, root.val, upper_bound)