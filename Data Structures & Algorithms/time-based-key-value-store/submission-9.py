class TimeMap:

    def __init__(self):
        self.timeStamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStamp:
            self.timeStamp[key] = []
        self.timeStamp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeStamp.keys():
            return ""
        left = 0
        right = len(self.timeStamp[key]) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.timeStamp[key][mid][1] <= timestamp:
                left = mid
            else:
                right = mid - 1
        return self.timeStamp[key][left][0] if self.timeStamp[key][left][1] <= timestamp else ""
