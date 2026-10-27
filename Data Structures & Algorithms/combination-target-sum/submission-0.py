class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, totalSum):
            if totalSum == target:
                res.append(path[:])
                return
            if totalSum > target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, totalSum + nums[i])
                path.pop()
        backtrack(0, 0)
        return res