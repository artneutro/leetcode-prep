# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Recursively substract the root.val from current targetSum 
        if root != None :
            # Once it reach the leaf check if the last substraction is zero
            if root.left == None and root.right == None :
                if targetSum - root.val == 0 :
                    return True
            # If is not a leaf then update the targetSum and send to children
            else :
                return self.hasPathSum(root.left, targetSum-root.val) \
                or self.hasPathSum(root.right, targetSum-root.val)
        return False
        
