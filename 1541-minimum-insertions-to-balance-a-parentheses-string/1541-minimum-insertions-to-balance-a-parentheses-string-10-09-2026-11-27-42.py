class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        seenL, seenR = [], []
        for let in s:
            if let == "(":
                if len(seenR) % 2: res += 1; seenR.append(")") 
                seenL.append("(")
            else:
                seenR.append(")")
                if not seenL or len(seenL)*2 < len(seenR):
                    res +=1
                    seenL.append("(")
        res = res + (len(seenL)*2 - len(seenR))
        return res