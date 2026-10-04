class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # x1, y1 [1] [2] bottom left 
        # x2, y2 [3] [4] top right 
        return not(rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1] or rec1[1] >= rec2[3])
        