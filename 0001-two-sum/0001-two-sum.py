class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, v in enumerate(nums):
            #i = index, v = value in list 
            if target - v in index:
            #if target - current num return current num and index in set 
                return [i, index[target-v]]
            #if not return then add to dict i = index, v = key 
            index[v] = i