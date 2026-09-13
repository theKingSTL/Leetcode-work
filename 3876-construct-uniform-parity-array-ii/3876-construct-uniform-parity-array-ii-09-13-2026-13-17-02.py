class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        countOdds, minimum = 0, float('inf')
        for i in range(len(nums1)):
            minimum = min(minimum, nums1[i])
            if nums1[i]%2 == 1:
                countOdds +=1
        if minimum%2 == 1:
            return True 
        if countOdds == 0:
            return True 
        return False 