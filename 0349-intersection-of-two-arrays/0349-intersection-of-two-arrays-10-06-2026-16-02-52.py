class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        if len(nums1) > len(nums2):
            nums1 = set(nums1)
            for n in nums2:
                if n in nums1:
                    res.append(n)
        else:
            nums2 = set(nums2)
            for n in nums1:
                if n in nums2:
                    res.append(n)
        return list(set(res))