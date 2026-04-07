# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # nice a completely new problem
        # essentially you can do a level order traversal 
        # and then take the rightmost element
        res = []
        self.dfs(root, 0, res)
        ret = []
        for nodes in res:
            ret.append(nodes[-1])
        return ret
    def dfs(self, root, depth, res):
        if not root:
            return
        if depth == len(res):
            res.append([])
        
        res[depth].append(root.val)
        self.dfs(root.left, depth+1, res)
        self.dfs(root.right, depth+1, res)