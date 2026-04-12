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
        copy = {}
        curr = head
        # all copy nodes now exist
        if not head:
            return None
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        # need to setup the links now 
        curr = head
        while curr:
            nxt = curr.next if curr.next else None
            rand = curr.random if curr.random else None
            copy_node = copy[curr]
            if nxt:
                copy_node.next = copy[nxt]
            if rand:
                copy_node.random = copy[rand]
            curr = curr.next
        return copy[head]
