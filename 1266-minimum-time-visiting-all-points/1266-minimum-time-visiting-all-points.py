class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #point 1 and point 2
        # movement int 
        # abs(point 2 x - point 1 x) magnitude away in x 
        # abs(point 2 y - point 2 y) magnitude away in y 

        #mx - my (if pos more x/ pure horiz to go, if negative need to go that vertical)
        #min(mx, my) gives how much diagonally we need to go 

        movement = 0
        for i in range(len(points)-1):
            mx = abs(points[i][0] - points[i+1][0])
            my = abs(points[i][1] - points[i+1][1])

            movement += min(mx,my) + abs(mx - my)
        
        return movement

