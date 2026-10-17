class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res += int((max(str(n)))*len(str(n)))
        return res
