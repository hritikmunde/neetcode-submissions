class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        output = [1] * n
        prefix = 1
        for i in range(n):
            prefix_product[i] = prefix
            prefix *= nums[i]     
        suffix = 1
        for i in range(n-1, -1, -1):
            suffix_product[i] = suffix
            suffix *= nums[i]
        for i in range(n):
            output[i] = prefix_product[i] * suffix_product[i]
        return output