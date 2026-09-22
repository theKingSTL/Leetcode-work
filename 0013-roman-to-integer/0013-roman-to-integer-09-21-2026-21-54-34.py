rDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            if rDict[s[i]] < rDict[s[i+1]] : res -= rDict[s[i]]
            else: res += rDict[s[i]]
        return res + rDict[s[-1]]