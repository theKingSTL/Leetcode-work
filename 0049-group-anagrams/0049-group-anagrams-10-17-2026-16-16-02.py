class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listRes = {}
        for s in strs:
            ana = str(''.join(sorted(s)))
            if ana in listRes:
                listRes[ana].append(s)
            else:
                listRes[ana] = [s]
        return list(listRes.values())