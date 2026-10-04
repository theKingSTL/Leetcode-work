class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curRes = 0
        for char in s:
            if char == "(": curRes +=1
            elif char == ")": 
                res = max(res, curRes)
                curRes -= 1
            else:
                pass
        return res
            

