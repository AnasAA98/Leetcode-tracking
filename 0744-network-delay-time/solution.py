class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [math.inf] * (n + 1)
        adj = defaultdict(list)
        for time in times:
            u,v,w = time
            adj[u].append((v,w))
        heap = []
        heap.append((0,k))
        heapq.heapify(heap)
        while heap:
            w,dest = heapq.heappop(heap)
            if w > dist[dest]:
                continue
            dist[dest] = w
            for v, weight in adj[dest]:
                new_dist = w + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
        res = max(dist[1:])
        return res if res != math.inf else -1
            

