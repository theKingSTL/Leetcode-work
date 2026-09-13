class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        c, m = 0, float('inf')
        for i in nums1:
            m = min(m, i)
            if i%2 == 1:
                c +=1
        if m%2 == 1 or c == 0:
            return True 
        return False 