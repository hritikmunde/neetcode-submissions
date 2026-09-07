class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myArr = []
        for i in nums:
            if i in myArr:
                return True
            myArr.append(i)
        return False
            