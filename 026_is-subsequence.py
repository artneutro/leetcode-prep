# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Use 2 pointers to iterate over once a match is found
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t) :
            if s[s_index] == t[t_index] :
                s_index = s_index+1
                t_index = t_index+1
            else :
                t_index = t_index+1
        if s_index == len(s) :
            return True
        else :
            return False

