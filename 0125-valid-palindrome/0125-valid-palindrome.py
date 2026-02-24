class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        if s is False:
            return True
        
        l, r = 0, len(s) - 1
        while l <= r:
            if s[r] == s[l]:
                r -=1
                l += 1
            else:
                return False 
        return True 
