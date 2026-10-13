class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = format(x, '032b')
        y = format(y, '032b')
        res = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                res += 1
        return res
