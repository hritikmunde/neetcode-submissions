class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNum = max(nums[:k])
        res = [maxNum]
        frequency = {}
        for i in range(k):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1
        
        left = 0
        right = k
        while right < len(nums):
            
            frequency[nums[right]] = frequency.get(nums[right], 0) + 1
            right += 1
            frequency[nums[left]] -= 1
            if frequency[nums[left]] == 0:
                del frequency[nums[left]]
            left += 1
            maxNum = max(frequency)
            res.append(maxNum)
        return res
