# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # so how do we do this one
        # it is based on pathing; we need to go to very end
        # so we use a dfs-based approach
        # nodes can be 
        # ah so the path means root -> ...intermediates... -> x
        # so if root is > x then that is not a good node
        # so to do this we just keep a running maximum; if hit x
        # and max greater than no good
        return self.dfs(root, root.val)

    def dfs(self, root, local_max):
        if not root:
            return 0
        if local_max <= root.val:
            print(root.val, local_max)
            return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
        else: # local_max > root.val
            return self.dfs(root.left, local_max) + self.dfs(root.right, local_max)
