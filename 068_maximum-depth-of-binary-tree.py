# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root != None :
            # Recursively check max between left and right + 1
            if root.left != None and root.right != None :
                return (max(self.maxDepth(root.left), self.maxDepth(root.right)))+1
            elif root.left != None :
                return self.maxDepth(root.left)+1
            elif root.right != None :
                return self.maxDepth(root.right)+1
            else :
                return 1
        else :
            return 0

