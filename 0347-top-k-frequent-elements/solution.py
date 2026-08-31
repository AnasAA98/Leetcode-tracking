class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = Counter(nums)
        heap = []
        for num, freq in my_map.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _,num in heap]

