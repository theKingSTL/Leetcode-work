from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def ways(cur: int) -> int:
            if cur == n:
                return 1
            if cur > n:
                return 0
            return ways(cur + 1) + ways(cur + 2)

        return ways(0)