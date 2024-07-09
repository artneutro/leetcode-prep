# https://leetcode.com/problems/basic-calculator/
class Solution:
    def calculate(self, s: str) -> int:
        # Base case
        if len(s) == 1 :
            return int(s)
        # Variable initialization
        index = 0
        numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        stack = []
        while index < len(s) :
            # If is a space, ignore
            if s[index] == ' ' :
                index += 1
            # If if operator, stack
            elif s[index] in ('+', '-') : 
                stack.append(s[index])
                index += 1
            # If close parenthesis, process all the remaining operations inside group
            elif s[index] in ('(', ')') : 
                if s[index] == '(' :
                    stack.append(s[index])
                else :
                    number = stack.pop()
                    if len(stack) > 0 and stack[-1] == '(' :
                        open_p = stack.pop()
                    # Iterate over numbers stacked
                    while len(stack) > 1 :
                        if stack[-1] in ('+', '-') : 
                            if stack[-1] == '-' and stack[-2] == '(' :
                                number *= -1
                                sign = stack.pop()
                                open_p = stack.pop()
                                continue
                            sign = stack.pop()
                            val1 = stack.pop()
                            val2 = number
                            if len(stack) > 0 and stack[-1] == '-' :
                                val1 *= -1
                                skip = stack.pop()
                            if sign == '+' :
                                number = val1+val2
                            else :
                                number = val1-val2
                        else :
                            break
                    stack.append(number)
                index += 1
            # If numbers, stack or process
            elif s[index] in numbers : 
                # Get the whole number
                number = s[index]
                index += 1
                # "2147483647"
                while index < len(s) and s[index] in numbers :
                    number += s[index]
                    index += 1
                # Convert to integer to store
                number = int(number)
                # Stack or process
                while len(stack) > 1 :
                    if stack[-1] in ('+', '-') : 
                        # Negative value group processing 
                        if stack[-2] == '(' :
                            number *= -1
                            sign = stack.pop()
                            open_p = stack.pop()
                            continue
                        sign = stack.pop()
                        val1 = stack.pop()
                        val2 = number
                        # "-2+ 1"
                        if len(stack) > 0 and stack[-1] == '-' :
                            val1 *= -1
                            skip = stack.pop()
                        # Process the final operation
                        if sign == '+' :
                            number = val1+val2
                        else :
                            number = val1-val2
                    else :
                        # No more chained operators found
                        break
                # Re-stack results
                stack.append(number)
        # Positive overall value (could be negative as well)
        if len(stack) == 1 :
            return int(stack[0])
        # Negative overall value (could be positive as well)
        else :
            return -1*stack[1]

