# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        index = 0
        while index < len(strs) :
            # Use the sorted version of the string as the key
            sorted_string = str(sorted(strs[index]))
            if sorted_string in result_dict :
                result_dict[sorted_string].append(strs[index])
            else :
                result_dict[sorted_string] = [strs[index]]
            index += 1
        return result_dict.values()

