# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove trailing spaces and split into a list
        s_array = s.split()
        # Create a new string with the list reversed
        result = ''
        for i in s_array[::-1] :
            result += i+' '
        # Return the string without the last space
        return result[:-1]

