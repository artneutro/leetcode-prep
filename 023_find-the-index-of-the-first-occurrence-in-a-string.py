# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        while index < len(haystack) :
            # Case when needle size is longer
            if len(needle) > len(haystack[index:]) :
                return -1
            internal_index = 0
            while index < len(haystack) and internal_index < len(needle) :
                # Case when coincidences are found
                if haystack[index] == needle[internal_index] :
                    index = index+1
                    internal_index = internal_index+1
                else :
                    index = index+1
                    break
            # Case when the string was found
            if internal_index == len(needle) :
                return index-internal_index
            index = index-internal_index
        # Case when the string was not found
        return -1
        
