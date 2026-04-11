# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res
        rem = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            temp = num1 + num2 + rem
            rem = temp // 10
            curr.next = ListNode(temp%10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        if rem > 0:
            curr.next = ListNode(rem)
        return res.next


