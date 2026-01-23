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
            # if my curr node has a child:
            if curr.child:
                # what if theres a node after the curr
                # will need to append it to the tail of the child linked list
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            # reach stage where if there was a child and i explored that linked list
            # need to connect it back to my previous .next
            # that means my curr.next = None
            if not curr.next and stack:
                node = stack.pop()
                curr.next = node
                node.prev = curr
            curr= curr.next
        return head
