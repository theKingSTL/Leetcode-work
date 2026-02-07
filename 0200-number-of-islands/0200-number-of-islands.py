class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        #start with no islands and we need a set for what in the matrix we have visted
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        #Used to fill in all cords visited for island 
        def bfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == "0":
                return         
            visited.add((r,c))
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        
        return islands


        
