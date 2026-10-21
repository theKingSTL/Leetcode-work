class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for s in string:
            if s in mapping.keys():
                if not stack or stack[-1] != mapping[s]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s)
        return not stack 

