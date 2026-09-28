"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        res = []
        while curr:
            if curr.child:
                if curr.next:
                    res.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            if not curr.next and res:
                node = res.pop()
                curr.next = node
                node.prev = curr
            
            curr = curr.next
        return head

