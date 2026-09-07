class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        sorted_values = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_values[:k]]