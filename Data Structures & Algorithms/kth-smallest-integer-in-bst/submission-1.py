# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # do not just go into coding...
    # so we should leverage the fact it's a BST
    # the first thing we should do is obtain the number of nodes?
    # is the height relevant?
    # ah we can do inorder traversal
    # so we go all the way left, record our current (ie subtract 1 from k)
    # then traverse right?
        arr = []
        self.dfs(root, k, arr)
        return arr[k-1]

    def dfs(self, root, k, arr):
        if not root:
            return 
        self.dfs(root.left, k, arr)
        arr.append(root.val)
        self.dfs(root.right, k, arr)

        
        




        