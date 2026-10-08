class Solution:
    cache = [[1]]
    def getRow(self, rowIndex: int) -> list[int]:
        while len(self.cache) <= rowIndex:
            for i in range(len(self.cache),rowIndex+1):
                self.cache.append([])
                for x in range(i+1):
                    if x == 0 or x == i:
                        self.cache[i].append(1)
                    else:
                        self.cache[i].append(self.cache[i-1][x-1]+self.cache[i-1][x])
        return self.cache[rowIndex]