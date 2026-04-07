# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left_list = []
        right_list = []
        self.dfs(p, left_list)
        self.dfs(q, right_list)

        return left_list==right_list


    def dfs(self, root, list_nodes):
        if not root:
            list_nodes.append(None)
            return
        list_nodes.append(root.val)
        self.dfs(root.left, list_nodes)
        self.dfs(root.right, list_nodes)