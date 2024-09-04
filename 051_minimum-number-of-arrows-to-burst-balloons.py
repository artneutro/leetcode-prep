# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 0
        # First sort the array based on X-start
        points.sort()
        # Base case
        if len(points) == 1 :
            return 1
        # Iterate from back to front checking if X-start is lower than previous X-end to consolidate intervals
        index = len(points)-1
        compare_index = index-1
        while compare_index >= 0 : 
            if points[index][0] <= points[compare_index][1] : 
                compare_index -= 1
            else :
                arrows += 1
                index = compare_index
                compare_index -= 1
        # If reach the end (start of array), it means it was merged or it is an isolated baloon
        arrows += 1
        return arrows
        
