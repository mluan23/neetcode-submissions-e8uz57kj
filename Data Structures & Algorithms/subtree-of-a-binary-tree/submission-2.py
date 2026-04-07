# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # think we can just run a dfs on the root and subroot, get an arr
        # to represent them, then we can check if the subroot is in the root;
        # i think if our traversal order is correct this should be fine
        # does a dfs/bfs approach work?
        # i think we just do post order traversal and we are good
        # so start at root. i guess we literally just go thru each tree and check if
        # they are equal; seems really slow but sure

        if not subRoot:
            return True
        if not root:
            return False
        # ah this meakes more sense
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    # q should always be the subroot
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        else:
            return False 

