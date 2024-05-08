# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Perform a PostOrder traversal on the tree and store the nodes values + levels as tuples
    def bfsPostLevel(self, root: Optional[TreeNode], traversal: List[int], level: int) -> List[int]:
        if root != None :
            traversal.append((root.val, level))
            self.bfsPostLevel(root.right, traversal, level+1)
            self.bfsPostLevel(root.left, traversal, level+1)
        return traversal
    # Use the bfsPostLevel definition to get the first element per level which is the first seen
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        traversal = self.bfsPostLevel(root, [], 0)
        index = 0
        level = 0
        while index < len(traversal) :
            if traversal[index][1] == level :
                output.append(traversal[index][0])
                level += 1
            index += 1
        return output

