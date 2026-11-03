class Solution:
    def minMoves(self, nums: List[int]) -> int:
        highest = max(nums)
        res = 0 
        for n in nums:
            res += highest - n
        return res