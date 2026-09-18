import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_rate = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            hours = self.total_hours(piles, mid)
            if hours <= h:
                min_rate = min(min_rate, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_rate


    def total_hours(self, piles, k):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/k)
        return total_hours