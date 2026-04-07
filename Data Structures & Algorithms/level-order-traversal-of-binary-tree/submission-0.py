# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.traverse(root, res, 0)
        return res
    def traverse(self, root, res, level):
        if not root:
            return
        if level == len(res):
            res.append([])
        res[level].append(root.val)

        self.traverse(root.left, res, level+1)
        self.traverse(root.right, res, level+1)

