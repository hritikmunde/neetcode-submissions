class TimeMap:

    def __init__(self):
        self.timeStamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStamp:
            self.timeStamp[key] = []
        self.timeStamp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeStamp.keys() or self.timeStamp[key][0][0] > timestamp:
            return ""
        values = self.timeStamp[key]
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:    
                left = mid + 1
            else:
                right = mid - 1
        return values[right][1]
