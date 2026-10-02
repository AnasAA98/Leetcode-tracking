# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get the middle of the list 
        # reverse that right half 
        # then rebuild the linked list by alternating
        
        # Step 1: Find mid of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        # Step 2: reverse second half
        prev = None
        curr = mid
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        slow.next = None
        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next
            curr1.next = curr2
            curr2.next = nxt1
            curr1 = nxt1
            curr2 = nxt2
        

