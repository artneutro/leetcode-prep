# https://leetcode.com/problems/text-justification/
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 
        solution = []
        index = 0
        while index < len(words) :
            # Initialize new iteration
            line = []
            line_len = 0
            # Get first word
            line.append(words[index])
            line_len = len(words[index])
            index += 1
            # Iterate to fill the line
            while index < len(words) and line_len+1+len(words[index]) <= maxWidth : 
                line.append(' ')
                line.append(words[index])
                line_len += 1+len(words[index])
                index += 1
            # Format the line
            if index == len(words) :
                # Last line
                while line_len < maxWidth :
                    line.append(' ')
                    line_len += 1
            else :
                # If word is alone, might need to add space at the end
                if len(line) == 1 :
                    if len(line[0]) < maxWidth :
                        line.append(' ')
                        line_len += 1
                    else :
                        line.append('')
                # Not last line, add extra spaces from left to right up to maxWidth
                odd_index = 1
                while line_len < maxWidth :
                    if odd_index >= len(line) :
                        odd_index = 1
                    else :
                        line[odd_index] += ' '
                        line_len += 1
                        odd_index += 2
            line = ''.join(line)
            solution.append(line)
        return solution

