class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [[1]]

        for i in range(1,rowIndex+1):
            res.append([])
            for x in range(i+1):
                if x == 0 or x == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][x-1]+res[i-1][x])
        return res[-1]