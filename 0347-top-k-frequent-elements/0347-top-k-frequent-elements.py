class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        returnList = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        sortedCount = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        iterSortedCount = iter(sortedCount.keys())
        for i in range(k):
            returnList.append(next(iterSortedCount))
        return returnList 

