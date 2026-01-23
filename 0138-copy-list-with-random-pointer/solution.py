"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        new_values = {}
        curr = head
        # create a copy of each node
        while curr:
            new_values[curr] =Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            node = new_values[curr]
            node.next = new_values[curr.next] if curr.next else None
            node.random = new_values[curr.random] if curr.random else None
            curr = curr.next
        return new_values[head]
        
        
