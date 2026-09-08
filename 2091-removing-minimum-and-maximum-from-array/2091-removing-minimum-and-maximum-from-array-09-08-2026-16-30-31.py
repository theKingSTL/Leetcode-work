class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        maxIndex = nums.index(max(nums))
        minIndex = nums.index(min(nums))
        n = len(nums)

        if maxIndex < minIndex:
            mCopy = maxIndex
            maxIndex = minIndex
            minIndex = mCopy
        
        o1 = maxIndex + 1 
        o2 = n - minIndex 
        o3 = (minIndex + 1)  + (n - maxIndex)

        return min(o1, o2, o3)


