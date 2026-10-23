class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        slow = 0
        fast = slow + 1
        while fast < len(prices):
            profit = prices[fast] - prices[slow]
            if profit < 0:
                slow += 1
            else:
                max_profit = max(max_profit, profit)
                fast += 1
        return max_profit