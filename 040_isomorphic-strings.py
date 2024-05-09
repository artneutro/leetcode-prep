# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        index = 0
        while index < len(s) :
            # If the character is not in the hashmaps then add the corresponding relation
            if s[index] not in s_map and t[index] not in t_map :
                s_map[s[index]] = t[index]
                t_map[t[index]] = s[index]
            # If the hashmaps has any of the characters then check if the relation is the same previously
            elif s[index] in s_map :
                if t[index] in t_map :
                    if s_map[s[index]] != t[index] or t_map[t[index]] != s[index] :
                        return False
                else : 
                    return False
            elif t[index] in t_map :
                if s[index] in s_map :
                    if s_map[s[index]] != t[index] or t_map[t[index]] != s[index] :
                        return False
                else : 
                    return False
            index += 1
        # Isomorphic only if it reach the end of both strings
        return True

