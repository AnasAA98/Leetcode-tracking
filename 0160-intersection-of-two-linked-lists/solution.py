# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(x: ListNode):
            n = 0
            while x:
                n += 1
                x = x.next
            return n
        lengthA, lengthB = length(headA), length(headB)
        a, b = headA, headB

        for _ in range(lengthA - lengthB):
            a = a.next
        for _ in range(lengthB - lengthA):
            b = b.next
        
        while a != b:
            a = a.next
            b = b.next
        return a
