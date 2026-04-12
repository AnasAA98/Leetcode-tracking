class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        freq = 0
        for key,v in count.items():
            heap.append((-v,key))
        heapq.heapify(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
