class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        heap = [(0, src, 0)]  # (cost, node, stops)
        best_stops = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if node in best_stops and best_stops[node] <= stops:
                continue
            best_stops[node] = stops

            if stops <= k:
                for nei, w in adj[node]:
                    heapq.heappush(heap, (cost + w, nei, stops + 1))

        return -1
