class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortedStrs = sorted(strs)
        result = ""
        first = sortedStrs[0]
        last = sortedStrs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                result = result + first[i]

            else:
                return result 
        return result 