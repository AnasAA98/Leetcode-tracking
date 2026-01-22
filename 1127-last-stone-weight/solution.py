class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        if len(heap) == 1:
            return -heap[0]
        while  len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x!=y:
                weight_dif = abs((-x)-(-y))
                heapq.heappush(heap, -weight_dif)
        return -heap[0] if heap else 0
        
