# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # id assume its some traversal order that can do this
        # well we know that for each eve,
        # there is only 1 node
        # hmm bfs is probably better here
        if not root:
            return None
        queue = deque()
        res = []
        queue.append(root)
        # res.append(root.val)
        while queue:
            length = len(queue)
            # add all children for the given level
            for i in range(length):
                cur_node = queue.popleft()
                if i == length - 1:
                    res.append(cur_node.val)
                # queue.append(cur_node)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return res


