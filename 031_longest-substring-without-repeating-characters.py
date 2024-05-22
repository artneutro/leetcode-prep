# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sta_index = 0
        end_index = 1
        max_size = 0
        # Base cases
        if len(s) == 0 :
            return 0
        elif len(s) == 1 :
            return 1
        # Use the moving window to check for the max size substring
        else :
            cur_sub = s[0]
            while end_index < len(s) :
                if s[end_index] in s[sta_index:end_index] :
                    # If a duplicated is found then check the size reached and store if max
                    if len(s[sta_index:end_index]) > max_size :
                        max_size = len(s[sta_index:end_index])
                    # Every time a duplicated char is found then move the start index up to the previous+1
                    while s[sta_index] != s[end_index] :
                        sta_index += 1
                    sta_index += 1
                end_index += 1
            # Case largest is the last found
            if len(s[sta_index:end_index]) > max_size :
                max_size = len(s[sta_index:end_index])
            return max_size

