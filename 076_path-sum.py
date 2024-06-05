# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSum(self, root: Optional[TreeNode], targetSum: int, cumulative: List[int]) -> bool:
    # Definition created to check once it reached a leaf if the cumulative sum is the same as the target
        if root != None :
            if root.left == None and root.right == None :
                if cumulative + root.val == targetSum :
                    return True
            else :
            # If is not a leaf then recursively send the cumulative to both children
                return self.checkSum(root.left, targetSum, cumulative+root.val) \
                or self.checkSum(root.right, targetSum, cumulative+root.val)
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkSum(root, targetSum, 0)

