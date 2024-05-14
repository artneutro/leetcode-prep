# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert to string for better mangement
        index = 0
        str_digits = ''
        while index < len(digits) :
            str_digits += str(digits[index])
            index += 1
        # Convert to int and sum 1, then convert back to string
        result = str(int(str_digits)+1)
        # Create the array again with the new value
        index = 0
        output = []
        while index < len(result) :
            output.append(int(result[index]))
            index += 1
        return output

