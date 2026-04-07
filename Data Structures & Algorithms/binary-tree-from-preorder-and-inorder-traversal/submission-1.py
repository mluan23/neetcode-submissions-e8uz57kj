# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # inorder first tells me leftmost 
    # preorder first elem tells the root elem
    # but inorder is good for finding parent
    # if preorder elem == inorder[i], what's that mean?
    
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        # got no idea wtf this problem is
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

    # so we know the preorder[0] is the root
    # and the inorder splits in half
    


