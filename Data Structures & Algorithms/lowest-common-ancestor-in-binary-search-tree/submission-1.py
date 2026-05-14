# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root, p, q)
    def dfs(self, root, p, q):
        # since a solution is guaranteed this should never happen
        if not root:
            return None
        # it a bst so it means this guy gotta the lca
        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
            return root
        # if we hit one of them it means must be lca as well;
        # the other case would catch otherwise
        if root.val == p.val or root == q.val:
            return root
        # we dont need p.val and q.val > since its guaranteed at this point
        if p.val > root.val:
            return self.dfs(root.right, p, q)
        if p.val < root.val:
            return self.dfs(root.left, p, q)

