class Solution:
    def singleNumber(self, ns: list[int]) -> int:
        r = 0
        for n in ns:
            r ^= n
        return r
