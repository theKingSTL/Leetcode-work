class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        res = [triangle[0]]
        for i in range(1, len(triangle)):
            res.append([])
            for j in range(i+1):
                if j == 0:
                    best = res[i-1][0]
                elif j == i:
                    best = res[i-1][j-1]
                else:
                    best = min(res[i-1][j-1], res[i-1][j])
                res[i].append(triangle[i][j] + best)
        return min(res[-1])

 
        