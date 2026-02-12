class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        l, r = 0, len(strX) - 1
        while strX[l] == strX[r]:
            l += 1
            r -= 1
            if l >= r:
                return True 
        return False 

        