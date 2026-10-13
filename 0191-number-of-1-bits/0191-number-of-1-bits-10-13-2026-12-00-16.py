class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n, 'b')
        res = 0
        for num in n:
            if num == "1":
                res += 1
        return res