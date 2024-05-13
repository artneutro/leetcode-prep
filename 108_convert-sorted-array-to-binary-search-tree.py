# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = None
        if len(nums) > 0 :
            mid = len(nums)//2
            root = TreeNode(nums[mid], None, None)
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

