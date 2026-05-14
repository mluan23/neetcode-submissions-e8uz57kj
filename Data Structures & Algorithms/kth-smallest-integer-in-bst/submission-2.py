# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # cant we just do a traversal and return k
        # yeah but thats O(n)
        # we can do log(n) since bst i would assume
        # well dam recommend is O(n)
        # ig thats why its 82% accept
        nodes = []
        self.dfs(root, nodes)
        return nodes[k-1].val
        
    
    def dfs(self, root, nodes):
        # should be doing the inorder traversal
        if not root:
            return
        self.dfs(root.left,nodes)
        nodes.append(root)
        self.dfs(root.right, nodes)

        