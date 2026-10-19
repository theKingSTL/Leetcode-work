from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def paths(r, c):
            if r == m and c == n:
                return 1
            if r > m or c > n:
                return 0
            return paths(r + 1, c) + paths(r, c + 1)
        return paths(1, 1)