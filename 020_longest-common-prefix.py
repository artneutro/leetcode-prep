# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ''
        index = 0
        if len(strs) == 1 :
            return strs[0]
        # Get min size
        min_size = 201
        while index < len(strs) :
            if len(strs[index]) < min_size :
                min_size = len(strs[index])
            index = index+1
        # Check all string prefixes
        index = 0
        while (index+1 < len(strs)) :
            internal_index = 0
            while internal_index < min_size :
                if strs[index][internal_index] == strs[index+1][internal_index] :
                    internal_index = internal_index+1
                else :
                    if longest == '' :
                        longest = strs[index][:internal_index]
                    elif len(longest) > internal_index :
                        longest = strs[index][:internal_index]
                    break
            # Case one element is same as the longest prefix
            if internal_index == min_size :
                if longest == '' :
                    longest = strs[index][:internal_index]
                elif len(longest) > internal_index :
                    longest = strs[index][:internal_index]
            print("AFTER INTERNAL", index, internal_index, longest, strs[index][:internal_index])
            # Case first and second elements are differents since char 0
            if internal_index == 0 :
                return ''
            index = index+1
        return longest

