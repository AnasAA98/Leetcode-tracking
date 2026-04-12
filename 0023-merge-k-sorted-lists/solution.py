# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) < 2:
            return lists[0]
        heap = []
        counter = 0
        for link in lists:
            curr = link
            while curr:
                heap.append((curr.val,counter,curr))
                counter+=1
                curr = curr.next
        if not heap: # if lists is populated with empty lists
            return None
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        while heap:
            curr.next = heapq.heappop(heap)[2]
            curr = curr.next
        curr.next = None
        return head.next
