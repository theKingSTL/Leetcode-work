class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numbers = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
            6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        ans, res = [x for x in numbers[int(digits[0])]], []
        for i, digit in enumerate(digits[1:], start=1):
            val, res = numbers[int(digits[i])], []
            for i in range(len(ans)):
                res = res + [ans[i]+x for x in val]
            ans = res
        return ans
