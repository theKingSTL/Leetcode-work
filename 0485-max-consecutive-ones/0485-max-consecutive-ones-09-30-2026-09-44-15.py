class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        result = 0
        reset = 0
        for n in range(len(nums)):
            if nums[n] == 1:
                reset += 1
            elif nums[n] == 0: 
                if reset > result:
                    result = reset
                reset = 0
        if reset > result:
            result = reset
        return result
