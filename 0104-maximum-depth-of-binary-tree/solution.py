# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return 1 + max(lh,rh)
        res = height(root)
        return res
