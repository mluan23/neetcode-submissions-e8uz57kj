# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # the intuitive way is to run a traversal method, store all nodes
        # then just do the same thing and compare the results
        # but i remember theres a better way to do it, where yoi
        # dont need to store nodes
        # id assume we can just traverse both trees at same time 
        # instead of doing one at a time, then just compare like that
        return self.dfs(p,q)

    def dfs(self, p, q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
        if p.val != q.val:
            return False
        return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)