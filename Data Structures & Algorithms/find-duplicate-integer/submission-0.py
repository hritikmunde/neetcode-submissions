class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = set()
        for num in nums:
            if num in hash_map:
                return num
            hash_map.add(num)