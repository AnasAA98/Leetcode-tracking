# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr1 = dummy
        curr = head
        curr_sum = 0
        curr = curr.next
        while curr:
            curr_sum += curr.val
            if curr.val == 0:
                curr1.next = ListNode(curr_sum)
                curr1 = curr1.next
                curr_sum = 0
            curr = curr.next
        return dummy.next



