class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda box: box[1], reverse = True)
        total = 0
        for count, units in boxTypes:
            if truckSize <= 0:
                break
            take = min(count, truckSize)
            total += take * units
            truckSize -= take
        return total 


