# https://leetcode.com/problems/construct-quad-tree/
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # When reach a leaf, return the Node with the value
        if len(grid) == 1 :
            if grid[0][0] == 0 :
                return Node(0, True)
            else :
                return Node(1, True)
        # Otherwise, construct recursively the 4 matrix sections
        else :
            top_left = self.construct([line[:int(len(grid)/2)] for line in grid[0:int(len(grid)/2)]])
            top_righ = self.construct([line[int(len(grid)/2):int(len(grid))] for line in grid[0:int(len(grid)/2)]])
            bot_left = self.construct([line[:int(len(grid)/2)] for line in grid[int(len(grid)/2):int(len(grid))]])
            bot_righ = self.construct([line[int(len(grid)/2):int(len(grid))] for line in grid[int(len(grid)/2):int(len(grid))]])
            # If all 4 sections are same, return the comprised Node
            if top_left.val == top_righ.val\
            and top_righ.val == bot_left.val\
            and bot_left.val == bot_righ.val :
                if top_left.val == 0 :
                    return Node(0, True)
                elif top_left.val == 1 :
                    return Node(1, True)
                else :
                    # Case that all 4 sub-matrixes are mixed
                    return Node(-1, False, top_left, top_righ, bot_left, bot_righ)
            # Case where one or more sub-matrixes are different
            else :
                return Node(-1, False, top_left, top_righ, bot_left, bot_righ)

