# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        res = 0
        def dfs(node,curr):
            if not node:
                return 0
            curr += node.val
            count = 1 if curr == targetSum else 0
            return count + dfs(node.left,curr)+ dfs(node.right,curr)
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                res += dfs(curr,0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res            
        
            
