class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsSort = sorted(nums)
        returnDict = {}
        for i, v in enumerate(numsSort):
            if i == 0:
                returnDict[v] = i 
            elif numsSort[i] == numsSort[i-1]:
                continue
            else:
                returnDict[v] = i 
        
        returnList = []
        for i in range(len(nums)):
            returnList.append(returnDict.get(nums[i]))
        
        return returnList


