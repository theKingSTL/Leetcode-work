class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumOfNums = sum(nums)
        compareTargetSum = sum(range(len(nums)+1))
        return compareTargetSum - sumOfNums