# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # to solve this we can just calc heights of the left and right subtrees
        # and check if they are differing in height 1 or not
        self.is_balanced = True
        self.dfs(root)


        return self.is_balanced

    def dfs(self, root):
        if not root:
            return 0
        
        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)

        if abs(left_height - right_height) > 1:
            self.is_balanced = False
        return 1+ max(self.dfs(root.left), self.dfs(root.right))
        
            