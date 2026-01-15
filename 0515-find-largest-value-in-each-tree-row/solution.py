# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        while q:
            max_row = -inf
            for _ in range(len(q)):
                curr = q.popleft()
                max_row = max(curr.val,max_row)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(max_row)
        return result

