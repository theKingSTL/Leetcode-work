class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1     
        seen = set(nums1)
        res = []
        for n in nums2:
            if n in seen:
                res.append(n)
                seen.remove(n)             
                if not seen:   
                    break              
        return res