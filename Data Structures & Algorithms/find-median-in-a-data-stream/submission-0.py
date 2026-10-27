import heapq
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        if len(self.nums) == 1:
            return self.nums[0]
        self.nums.sort()
        if len(self.nums) % 2 == 0:
            mid = len(self.nums) // 2
            return (self.nums[mid-1] + self.nums[mid]) / 2
        else:
            mid = len(self.nums) // 2
            return self.nums[mid]
        