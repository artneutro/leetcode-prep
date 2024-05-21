# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        index = 0
        while index*index <= x :
            index += 1
        return index-1

