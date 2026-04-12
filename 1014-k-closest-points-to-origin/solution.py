class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pair in points:
            x,y = pair
            dist = x**2 + y**2
            heap.append((dist,pair))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

