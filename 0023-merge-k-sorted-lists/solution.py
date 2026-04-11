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
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                heap.append((curr.val,counter,curr))
                counter+=1
                curr = curr.next
        if not heap:
           return None
        heapq.heapify(heap)
        head = heapq.heappop(heap)[2]
        prev = head
        while heap:
            prev.next = heapq.heappop(heap)[2]
            prev = prev.next
        prev.next = None
        return head
        


        
