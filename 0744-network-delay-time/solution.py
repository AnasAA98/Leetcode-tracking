class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        dist = {} # check for visited nodes
        heap = [(0,k)]
        heapq.heapify(heap)
        while heap:
            w,v = heapq.heappop(heap)
            if v in dist:
                continue
            dist[v]= w
            for v1,w1 in adj[v]:
                if v1 not in dist:
                    heapq.heappush(heap,(w + w1, v1))
        if len(dist) != n:
            return -1
        return max(dist.values())




