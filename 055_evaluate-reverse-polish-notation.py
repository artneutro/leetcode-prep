# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Variables initialization
        operators = ['+', '-', '*', '/']
        stack = []
        solution = 0
        # Iterate over the values and operator and append or pop accordingly
        index = 0
        while index < len(tokens) :
            if tokens[index] in operators :
                item2 = int(stack.pop())
                item1 = int(stack.pop())
                result = 0
                if tokens[index] == '+' :
                    result = item1 + item2
                    stack.append(result)
                elif tokens[index] == '-' :
                    result = item1 - item2
                    stack.append(result)
                elif tokens[index] == '*' :
                    result = item1 * item2
                    stack.append(result)
                elif tokens[index] == '/' :
                    result = int(item1 / item2)
                    stack.append(result)
            else :
                stack.append(tokens[index])
            index += 1
        # Return the only value in the stack at the end of the process
        return int(stack.pop())

