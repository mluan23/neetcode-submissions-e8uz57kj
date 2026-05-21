# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root,p,q)
    def dfs(self, node, p, q):
        # since it is bst
        # we know that if the current node is == to p or q,
        # must be an ancestor
        if not node:
            return None
        if node.val == p.val or node.val == q.val:
            return node
        if (node.val < p.val and node.val > q.val) or (node.val < q.val and node.val > p.val):
            return node
        # otherwise we have to recurse left and right
        # if the current node is larger
        # then it means we need to check the left
        if node.val > p.val and node.val > q.val:
            return self.dfs(node.left, p, q)
        if node.val < p.val and node.val < q.val:
            return self.dfs(node.right, p, q)
        return node
        