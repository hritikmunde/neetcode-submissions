class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        result = sorted(frequency_map.keys(), key=lambda x: frequency_map[x], reverse=True)
        return result[:k]