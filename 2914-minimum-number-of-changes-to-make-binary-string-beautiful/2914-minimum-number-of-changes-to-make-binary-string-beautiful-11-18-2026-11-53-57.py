class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(len(s)//2):
            tec = i*2
            if s[tec] != s[tec+1]:
                res += 1
        return res  