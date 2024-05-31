# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Store the level values on a hashmap
    def bfsAvgLevels(self, root: Optional[TreeNode], level: int, hashmap_levels: Optional[int]) -> List[float]:
        if root != None :
            if level in hashmap_levels :
                hashmap_levels[level].append(root.val)
            else :
                hashmap_levels[level] = [root.val]
            self.bfsAvgLevels(root.left, level+1, hashmap_levels)
            self.bfsAvgLevels(root.right, level+1, hashmap_levels)
    # Use the hashmap to check the average per level
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        hashmap_levels = {}
        solution = []
        self.bfsAvgLevels(root, 0, hashmap_levels)
        for i in hashmap_levels :
            values_list = hashmap_levels[i]
            solution.append(sum(values_list)/len(values_list))
        return solution

