class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0 
        l,r = 0, len(height)-1
        while l < r:
            w = r - l
            h = min(height[l],height[r])
            maxWater = max(maxWater, h*w)
            if h == height[l]:
                l +=1
            else:
                r -=1
        return maxWater