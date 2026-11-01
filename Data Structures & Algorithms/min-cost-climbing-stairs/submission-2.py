class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev = cost[1]
        prevprev = cost[0]
        for i in range(2, n):
            curr = min(prev, prevprev) + cost[i]
            prevprev = prev
            prev = curr
        return min(prev, prevprev)