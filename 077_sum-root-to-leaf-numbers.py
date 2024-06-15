# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Definition created to keep a cumulative sum
    def sumNumbersCumulative(self, root: Optional[TreeNode], sofar: int) -> int:
        # If reached a leaf, return the sum so far + current value
        if root.left == None and root.right == None : 
            return sofar+root.val
        elif root.left == None : 
            return self.sumNumbersCumulative(root.right, (sofar*10)+(root.val*10))
        elif root.right == None : 
            return self.sumNumbersCumulative(root.left, (sofar*10)+(root.val*10))
        # Otherwise, return the sum of the values added up from both children 
        else :
            return self.sumNumbersCumulative(root.left, (sofar*10)+(root.val*10))\
            +self.sumNumbersCumulative(root.right, (sofar*10)+(root.val*10))
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        else :
            return self.sumNumbersCumulative(root, 0)

