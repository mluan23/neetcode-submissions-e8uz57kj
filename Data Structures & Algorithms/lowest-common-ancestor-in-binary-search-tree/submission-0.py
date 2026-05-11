# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # what does it mean to be a lca
        # we know that the topmost node is guaranteed to be an ancestor
        # all nodes unique
        # if you ever hit p or q it means the given node is the lowest node that
        # can be lca
        # it means that guy is lca or something higher
        # we could just keep a lowest var?
        # well no, you dont know where the splits are
        # so the splits are the most important due to it
        # being a bst
        return self.dfs(p,q,root)


    def dfs(self, p, q, root):
        # because of that early stopping essentially
        # what do we do for a none check though
        if root.val == p.val or root.val == q.val:
            return root
        if p.val > root.val and q.val > root.val:
            return self.dfs(p,q,root.right)
        if p.val < root.val and q.val < root.val:
            return self.dfs(p,q,root.left)
        # the last case is p < root and q > root or vice versa
        # in that case always return current node?
        return root