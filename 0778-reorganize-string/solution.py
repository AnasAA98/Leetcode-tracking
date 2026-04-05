class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        for k,c in freq.items():
            heap.append((-c,k))
        heapq.heapify(heap)
        res = []
        prev = None
        while heap:
            curr = heapq.heappop(heap)
            res.append(curr[1])
            if prev and prev[0] < 0:
                heapq.heappush(heap,prev)
            prev = (curr[0]+1,curr[1])
        if prev and prev[0] < 0:
            return ""
        return "".join(res)


