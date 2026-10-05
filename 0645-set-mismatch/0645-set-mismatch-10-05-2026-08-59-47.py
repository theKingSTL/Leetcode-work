class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        setNums = set(nums)
        dup = None
        
        for i, n in enumerate(nums):
            if n == dup:
                dup = n
                break
            dup = n
        for i in range(len(nums)):
            if i+1 in setNums:
                pass
            else:
                return [dup, i+1]
                
        