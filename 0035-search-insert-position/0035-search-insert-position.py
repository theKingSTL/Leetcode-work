class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        floor = 0
        ceil = len(nums) - 1

        while floor <= ceil:
            lookVal = (floor + ceil) // 2

            if nums[lookVal] == target:
                return lookVal
            elif nums[lookVal] > target:
                ceil = lookVal - 1
            else:
                floor = lookVal + 1

        return floor
