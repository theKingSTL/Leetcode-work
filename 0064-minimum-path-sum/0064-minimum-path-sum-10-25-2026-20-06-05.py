import functools

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(maxsize=None)
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if i == m - 1:
                return grid[i][j] + dp(i, j + 1)
            if j == n - 1:
                return grid[i][j] + dp(i + 1, j)
            return grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)