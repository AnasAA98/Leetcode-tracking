# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return isSame(a.left, b.left) and isSame(a.right, b.right)

        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == subRoot.val and isSame(curr, subRoot):
                return True
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return False

