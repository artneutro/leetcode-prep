# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the sentence and return the lenght of last word
        words = s.split()
        return len(words[-1])

