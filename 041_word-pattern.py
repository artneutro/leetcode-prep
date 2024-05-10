# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        s_map = {}
        pattern_map = {}
        index = 0
        if len(s_list) != len(pattern) :
            return False
        while index < len(s_list) :
            # If the character is not in the hashmaps then add the corresponding relation
            if s_list[index] not in s_map and pattern[index] not in pattern_map :
                s_map[s_list[index]] = pattern[index]
                pattern_map[pattern[index]] = s_list[index]
            # If the hashmaps has any of the characters then check if the relation is the same previously
            elif s_list[index] in s_map :
                if pattern[index] in pattern_map :
                    if s_map[s_list[index]] != pattern[index] or pattern_map[pattern[index]] != s_list[index] :
                        return False
                else : 
                    return False
            elif pattern[index] in pattern_map :
                if s_list[index] in s_map :
                    if s_map[s_list[index]] != pattern[index] or pattern_map[pattern[index]] != s_list[index] :
                        return False
                else : 
                    return False
            index += 1
        # Isomorphic only if it reach the end of both strings
        return True

