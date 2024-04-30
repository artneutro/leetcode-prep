# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        year = str(num)
        answer = ''
        # 1 
        if len(year) > 0 :
            if year[-1] == '1' :
                answer = 'I' + answer
            if year[-1] == '2' :
                answer = 'II' + answer
            if year[-1] == '3' :
                answer = 'III' + answer
            if year[-1] == '4' :
                answer = 'IV' + answer
            if year[-1] == '5' :
                answer = 'V' + answer
            if year[-1] == '6' :
                answer = 'VI' + answer
            if year[-1] == '7' :
                answer = 'VII' + answer
            if year[-1] == '8' :
                answer = 'VIII' + answer
            if year[-1] == '9' :
                answer = 'IX' + answer
            year = year[:len(year)-1]
        # 10
        if len(year) > 0 :
            if year[-1] == '1' :
                answer = 'X' + answer
            if year[-1] == '2' :
                answer = 'XX' + answer
            if year[-1] == '3' :
                answer = 'XXX' + answer
            if year[-1] == '4' :
                answer = 'XL' + answer
            if year[-1] == '5' :
                answer = 'L' + answer
            if year[-1] == '6' :
                answer = 'LX' + answer
            if year[-1] == '7' :
                answer = 'LXX' + answer
            if year[-1] == '8' :
                answer = 'LXXX' + answer
            if year[-1] == '9' :
                answer = 'XC' + answer
            year = year[:len(year)-1]
        # 100
        if len(year) > 0 :
            if year[-1] == '1' :
                answer = 'C' + answer
            if year[-1] == '2' :
                answer = 'CC' + answer
            if year[-1] == '3' :
                answer = 'CCC' + answer
            if year[-1] == '4' :
                answer = 'CD' + answer
            if year[-1] == '5' :
                answer = 'D' + answer
            if year[-1] == '6' :
                answer = 'DC' + answer
            if year[-1] == '7' :
                answer = 'DCC' + answer
            if year[-1] == '8' :
                answer = 'DCCC' + answer
            if year[-1] == '9' :
                answer = 'CM' + answer
            year = year[:len(year)-1]
        # 1000
        if len(year) > 0 :
            if year[-1] == '1' :
                answer = 'M' + answer
            if year[-1] == '2' :
                answer = 'MM' + answer
            if year[-1] == '3' :
                answer = 'MMM' + answer
            # Max constraint 3999
            year = year[:len(year)-1]
        return answer
