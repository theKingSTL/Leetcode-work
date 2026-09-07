class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listRes = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in listRes:
                listRes[key] = []
            listRes[key].append(s)

        return list(listRes.values())
            
            


             
