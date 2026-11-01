class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 1
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
        return second