# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        index = 0
        check = []
        # Use a stack to check the correctness
        while index < len(s) :
            if s[index] == '(' \
            or s[index] == '{' \
            or s[index] == '[' :
                check.append(s[index])
            elif len(check) != 0 and s[index] == ')' :
                if check[-1] == '(' :
                    check.pop()
                else :
                    return False
            elif len(check) != 0 and s[index] == '}' :
                if check[-1] == '{' :
                    check.pop()
                else :
                    return False
            elif len(check) != 0 and s[index] == ']' :
                if check[-1] == '[' :
                    check.pop()
                else :
                    return False
            else :
                return False
            index += 1
        # Check if there were remaining opened
        if len(check) != 0 :
            return False
        # Valid only if all were closed in correct order
        return True

