"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            path = []
            for _ in range(len(q)):
                curr = q.popleft()
                path.append(curr.val)
                if curr.children:
                    for child in curr.children:
                        q.append(child)
            result.append(path)
        return result
         

