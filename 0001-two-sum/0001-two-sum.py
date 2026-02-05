class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    break
                elif nums[i] + nums[j] == target:
                    lis = [i,j]
                    return lis
