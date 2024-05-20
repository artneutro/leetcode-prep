# https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # The result is SUM(n/(5*i)) with i from 1 to n increasing by a delta of 5
        result = 0
        denominator = 5
        while denominator <= n : 
            k = int(n/denominator)
            result += k
            denominator *= 5
        return result

