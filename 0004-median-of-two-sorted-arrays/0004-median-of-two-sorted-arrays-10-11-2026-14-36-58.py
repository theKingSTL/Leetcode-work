class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res = []
        i, j = 0, 0
        while i != len(nums1) and j !=len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i == len(nums1) and j != len(nums2):
            res += nums2[j:]
        if j == len(nums2) and i != len(nums1):
            res += nums1[i:]
        
        size = len(res)
        odd = size%2
        mid = size//2

        if odd:
            return float(res[mid])
        else:
            return float((res[mid]+res[mid-1])/2)
