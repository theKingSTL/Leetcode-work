class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        def shift(img, dx, dy):
            shifted = [[0] * n for i in range(n)]
            for i in range(n):
                for j in range(n):
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        shifted[ni][nj] = img[i][j]
            return shifted

        def match(i1, i2):
            a = 0
            for i in range(n):
                for j in range(n):
                    if i1[i][j] == 1 and i2[i][j] == 1:
                        a += 1
            return a

        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                shifted_img2 = shift(img2, dx, dy)
                overlap = match(img1, shifted_img2)
                ans = max(ans, overlap)
        return ans