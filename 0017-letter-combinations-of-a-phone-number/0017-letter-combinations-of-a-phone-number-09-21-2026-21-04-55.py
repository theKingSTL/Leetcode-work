class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numbers = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
            6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        ans = []
        for i, digit in enumerate(digits):
            val = numbers[int(digits[i])]
            if i == 0:
                ans = [x for x in val]
            else:
                res = []
                for i in range(len(val)):
                    res = res + [x+val[i] for x in ans]
                ans = res
        return ans
