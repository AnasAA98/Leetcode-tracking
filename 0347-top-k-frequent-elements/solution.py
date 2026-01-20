class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-freq[num], num) for num in freq]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


