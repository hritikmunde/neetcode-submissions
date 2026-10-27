import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y:
                continue
            elif y < x:
                heapq.heappush(heap, -(x-y))
        if len(heap) == 1:
            return -heapq.heappop(heap)
        else:
            return 0