class Solution:
    def romanToInt(self, s: str) -> int:
        rDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i, letter in enumerate(s[:-1]):
            if rDict[letter] < rDict[s[i+1]] : res = res - rDict[letter]
            else: res = res + rDict[letter]
        res = res + rDict[s[-1]]
        return res