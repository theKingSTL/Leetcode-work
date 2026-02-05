class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        returnList = []

        for i in range (1,len(nums)+1):
            if i not in numSet:
                returnList.append(i)
        
        return returnList