# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        # Not using hashmap
        n_str = str(n)
        output = 0
        counter = 0
        while output != 1 :
            index = 0
            squares = 0
            while index < len(n_str) :
                squares += int(n_str[index])*int(n_str[index])
                index += 1
            n_str = str(squares)
            output = squares
            counter += 1
            # Break the infinite loop
            if counter > 1000 :
                return False
        return True

