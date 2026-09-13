class Solution:
    def uniformArray(self, n: list[int]) -> bool:
        c = 0
        if min(n)%2 == 1:
            return True
        for i in n:
            if i%2 == 1:
                c +=1
        if c == 0:
            return True 
        return False 