class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]

        for i in range(1,numRows):
            res.append([])
            for x in range(i+1):
                if x == 0 or x == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][x-1]+res[i-1][x])
        return res 

