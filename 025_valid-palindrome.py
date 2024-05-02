# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ini = 0
        end = len(s)-1
        # Check until the 2 pointers crossed
        while ini<end :
            # Look for the next alnum from left
            while (ini<end and not s[ini].isalnum()) :
                ini = ini+1
            # Look for next alnum from right
            while (ini<end and not s[end].isalnum()) :
                end = end-1
            # Check equality
            if s[ini] != s[end] :
                return False
            else :
                ini = ini+1
                end = end-1
        return True

