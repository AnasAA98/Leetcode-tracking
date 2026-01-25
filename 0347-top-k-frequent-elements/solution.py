class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-val,num) for num,val in freq.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range((k))]


