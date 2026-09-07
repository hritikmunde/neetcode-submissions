class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        myArr = []
        for i in range (len(nums)):
            diff = target - nums[i]

            if diff in myMap:
                myArr.append(myMap[diff])
                myArr.append(i)
                return myArr
            myMap[nums[i]] = i  