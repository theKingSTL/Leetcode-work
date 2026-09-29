class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            result = int("".join(map(str, digits)))
            result += 1
            digits = list(map(int, str(result)))
        else:
            digits[-1] = digits[-1] + 1
        return digits 