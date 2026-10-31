import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float("inf")] * (n+1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nxt, w in graph[node]:
                nd = d + w
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    heapq.heappush(heap, (nd, nxt))
        ans = max(dist[1:])
        return ans if ans != float("inf") else -1