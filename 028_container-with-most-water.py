# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Max capacity height for both sides (not necesarily the higher value)
        max_left = 0
        max_right = 0
        # Current indexes iterating the height array
        index_left = 0
        index_right = len(height)-1
        # Variable to store the max capacity found so far
        max_capacity = 0
        # Iterate to find the max capacity possible
        while index_left < index_right :
            # Check if the new area is higher than the current max
            if ((index_right - index_left) * min(height[index_right], height[index_left])) > max_capacity :
                max_left = index_left
                max_right = index_right
                max_capacity = (index_right - index_left) * min(height[index_right], height[index_left])
            # Move the lower index 
            if height[index_left] <= height[index_right] :
                index_left += 1
            else :
                index_right -= 1
        return max_capacity
        
        
