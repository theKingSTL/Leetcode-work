class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        c = 0
        if min(nums1)%2 == 1:
            return True
        for i in nums1:
            if i%2 == 1:
                c +=1
        if c == 0:
            return True 
        return False 