class Solution:
    def checkValidString(self, s: str) -> bool:
        opens, stars = [], []
        for i, c in enumerate(s):
            if c == "(":
                opens.append(i)
            elif c == "*":
                stars.append(i)
            else:
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while opens and stars:
            if opens.pop() > stars.pop():
                return False
        return not opens