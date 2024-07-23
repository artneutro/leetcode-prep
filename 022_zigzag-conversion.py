# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base case
        if numRows == 1 :
            return s
        final_string = ''
        # Create a list of numRows strings
        solution = ['' for x in range(numRows)]
        up_or_down = 1
        cur_row = 0
        index = 0
        while index < len(s) :
            # Append on proper internal string
            solution[cur_row] += (s[index])
            # If cur_row reached upper bound, reverse direction
            if cur_row == 0 :
                up_or_down = 1
            # If cur_row reached lower bound, reverse direction
            elif cur_row == len(solution)-1 :
                up_or_down = -1
            # Increase or decrease depending on direction
            if up_or_down == 1 :
                cur_row += 1
            else :
                cur_row -= 1
            index += 1
        # Append all strings to create the final_string
        index = 0
        while index < len(solution) :
            final_string += solution[index]
            index += 1
        return final_string

