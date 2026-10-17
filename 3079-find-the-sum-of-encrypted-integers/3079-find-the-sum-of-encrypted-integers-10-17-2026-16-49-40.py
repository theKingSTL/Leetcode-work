class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(int(max(str(n)) * len(str(n))) for n in nums)