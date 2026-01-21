# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        # now build the tree based on the ordered values
        def build(lo,hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nodes[mid])
            node.left = build (lo,mid-1)
            node.right= build (mid+1,hi)
            return node
        return build(0,len(nodes)-1)
