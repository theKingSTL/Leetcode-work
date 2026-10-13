class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        n = len(sq)
        neg = n // 2                 
        return sum(sq[neg:]) - sum(sq[:neg])



