class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    backtrack(path)
                    path.pop()
                    visited.remove(nums[i])
        backtrack([])
        return res
