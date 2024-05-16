# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def recursiveCombinations(self, digits: str, current: List[str], values: dict) -> List[str]:
        # Recursively add all the combinations from the current list to the next digit possible values
        result = []
        for i in current :
            for j in values[int(digits[0])] :
                result.append(i+j) 
        if len(digits) > 1 :
            return self.recursiveCombinations(digits[1:], result, values)
        else :
            return result
    def letterCombinations(self, digits: str) -> List[str]:
        possible_values = {}
        possible_values[2] = ['a', 'b', 'c']
        possible_values[3] = ['d', 'e', 'f']
        possible_values[4] = ['g', 'h', 'i']
        possible_values[5] = ['j', 'k', 'l']
        possible_values[6] = ['m', 'n', 'o']
        possible_values[7] = ['p', 'q', 'r', 's']
        possible_values[8] = ['t', 'u', 'v']
        possible_values[9] = ['w', 'x', 'y', 'z']
        if len(digits) == 0 :
            return []
        elif len(digits) == 1 :
            return possible_values[int(digits)]
        else :
            return self.recursiveCombinations(digits[1:], possible_values[int(digits[0])], possible_values)

