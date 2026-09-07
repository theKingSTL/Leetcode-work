class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listRes = {}
        for s in strs:
            listRes.setdefault(''.join(sorted(s)), []).append(s)
        return list(listRes.values())
            
            


             
