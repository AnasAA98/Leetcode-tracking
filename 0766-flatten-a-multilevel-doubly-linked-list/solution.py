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
        stack = []
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.child.prev = curr
                curr.next = curr.child
                curr.child = None
            if not curr.next and stack:
                new_node = stack.pop()
                curr.next = new_node
                new_node.prev = curr
            curr = curr.next
            

        return head

