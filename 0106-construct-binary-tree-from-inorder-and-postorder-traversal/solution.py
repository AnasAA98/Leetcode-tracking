# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        left_inorder = inorder[:mid]
        right_inorder = inorder[mid+1:]
        
        left_postorder = postorder[: mid]
        right_postorder = postorder[mid:-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
