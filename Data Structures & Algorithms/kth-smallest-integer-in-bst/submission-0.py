# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elems = []
        self.traverse(root, elems)
        return elems[k-1]

    def traverse(self, root, elems):
        if not root:
            return
        self.traverse(root.left, elems)
        elems.append((root.val))
        self.traverse(root.right,elems)
