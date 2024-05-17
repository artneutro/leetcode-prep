# https://leetcode.com/problems/triangle/
class Solution:
    def recursiveTotal(self, triangle: List[List[int]], cumulative: List[int]) -> int:
        # If the triangle is finished return the minimum accumulated
        if len(triangle) == 0 :
            return min(cumulative)
        # Else recursively get min sum of each next element with related cumulatives
        else :
            new_cumulative = []
            index = 0
            while index < len(triangle[-1]) :
                new_min = min(triangle[-1][index]+cumulative[index], \
                              triangle[-1][index]+cumulative[index+1])
                new_cumulative.append(new_min)
                index += 1
            return self.recursiveTotal(triangle[:-1], new_cumulative)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.recursiveTotal(triangle[:-1], triangle[-1])

