# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Definition of recursive DFS including dynamic traversal array
    def dfsPreOrder(self, root: Optional[TreeNode], traversal: List[int]) -> List[int]:
        if root != None :
            self.dfsPreOrder(root.left, traversal)
            traversal.append(root.val)
            self.dfsPreOrder(root.right, traversal)
        return traversal
    # As its a BST use the traversal to quickly find the minimum absolute difference
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        traversal = self.dfsPreOrder(root, [])
        index = 0
        min_diff = None
        while index+1 < len(traversal) :
            new_diff = abs(traversal[index]-traversal[index+1]) 
            if min_diff == None :
                min_diff = new_diff
            elif min_diff > new_diff :
                min_diff = new_diff
            index += 1
        return min_diff

