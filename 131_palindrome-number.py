# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        index_ini = 0
        index_end = len(x_str)-1
        while index_ini < index_end :
            if x_str[index_ini] != x_str[index_end] :
                return False
            index_ini += 1
            index_end -= 1
        return True

