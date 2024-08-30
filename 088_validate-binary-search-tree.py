# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxValue(self, root: Optional[TreeNode]) -> int:
        # Get the max value of a Tree
        max_val = 0
        if root != None :
            max_val = root.val
            if root.left != None :
                left_max = self.maxValue(root.left)
                if left_max > max_val : 
                    max_val = left_max
            if root.right != None :
                right_max = self.maxValue(root.right)
                if right_max > max_val : 
                    max_val = right_max
        return max_val
    def minValue(self, root: Optional[TreeNode]) -> int:
        # Get the min value of a Tree
        min_val = 10001
        if root != None :
            min_val = root.val
            if root.left != None :
                left_min = self.minValue(root.left)
                if left_min < min_val : 
                    min_val = left_min
            if root.right != None :
                right_min = self.minValue(root.right)
                if right_min < min_val : 
                    min_val = right_min
        return min_val
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root != None :
            # Check current node compared to max value on left and min value on right
            if root.left != None :
                if self.maxValue(root.left) >= root.val :
                    return False
            if root.right != None :
                if self.minValue(root.right) <= root.val :
                    return False
            # If they are fine, then check the subtrees
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        # If None, return True
        return True

