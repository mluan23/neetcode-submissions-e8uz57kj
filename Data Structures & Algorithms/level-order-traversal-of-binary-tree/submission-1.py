# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # for this we can run a DFS, and also keep a level variable
        # since it's left to right yeah dfs should work?
        # and we can do a sort of preorder traversal?
        res = []
        self.dfs(root, res, 1)
        return res

    def dfs(self, root, res, level):
        # do nothing if null
        if not root:
            return
        # every time we encounter a new level we can add 
        # a new array
        if len(res) < level:
            res.append([])
        res[level-1].append(root.val)
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)

