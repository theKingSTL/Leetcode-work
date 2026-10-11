class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                res.append(nums1.pop(0))
            else:
                res.append(nums2.pop(0))
        if nums1:
            res += nums1
        if nums2:
            res += nums2
        
        size = len(res)
        odd = size%2
        mid = size//2

        if odd:
            return float(res[mid])
        else:
            return float((res[mid]+res[mid-1])/2)
