class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookedUp = set()
        for i, num in enumerate(nums):
            if num in lookedUp:
                return True
            else:
                lookedUp.add(num)
                if len(lookedUp)>k:
                    lookedUp.remove(nums[i-k])
        return False 

