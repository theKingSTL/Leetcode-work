class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda box: box[1], reverse = True)
        ans = 0
        boxUses = boxTypes
        for i in range(truckSize):
            if boxUses == []:
                return ans
            ans += boxUses[0][1]
            boxUses[0][0] = boxUses[0][0] - 1
            if boxUses[0][0] == 0:
                boxUses.pop(0)
        return ans


