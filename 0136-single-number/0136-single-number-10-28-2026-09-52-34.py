class Solution:
    def singleNumber(self, numbers: list[int]) -> int:
        returnValueForSingleNumberDef = 0
        for number in numbers:
            returnValueForSingleNumberDef ^= number
        return returnValueForSingleNumberDef
