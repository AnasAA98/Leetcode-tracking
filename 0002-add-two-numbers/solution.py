# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        head = dummy
        rem = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            curr = n1 + n2 + rem
            rem = curr // 10
            head.next = ListNode(curr % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            head = head.next
        if rem > 0:
            head.next = ListNode(rem)
        return dummy.next
            
