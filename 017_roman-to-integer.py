# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        # Iterate over the Roman digits and follow the transformation rules
        count = 0
        index = 0
        while index < len(s):
            if s[index] == 'I' :
                if index+1 < len(s) and s[index+1] == 'V' : 
                    count = count+4
                    index = index+2
                elif index+1 < len(s) and s[index+1] == 'X' :
                    count = count+9
                    index = index+2
                else :
                    count = count+1
                    index = index+1
            elif s[index] == 'V' :
                count = count+5
                index = index+1
            elif s[index] == 'X' :
                if index+1 < len(s) and s[index+1] == 'L' : 
                    count = count+40
                    index = index+2
                elif index+1 < len(s) and s[index+1] == 'C' :
                    count = count+90
                    index = index+2
                else :
                    count = count+10
                    index = index+1
            elif s[index] == 'L' :
                count = count+50
                index = index+1
            elif s[index] == 'C' :                
                if index+1 < len(s) and s[index+1] == 'D' : 
                    count = count+400
                    index = index+2
                elif index+1 < len(s) and s[index+1] == 'M' :
                    count = count+900
                    index = index+2
                else :
                    count = count+100
                    index = index+1
            elif s[index] == 'D' :
                count = count+500
                index = index+1
            elif s[index] == 'M' :
                count = count+1000
                index = index+1
        return count
