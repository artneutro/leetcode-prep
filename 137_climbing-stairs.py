# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n in range(1,4) :
            return n
        else :
            index = 2
            result = 1
            new_result = 2
            while (index <= n) :
                if (index == n) :
                    return max(result, new_result)
                else :
                    if result > new_result :
                        new_result += result
                    else :
                        result += new_result
                index += 1

