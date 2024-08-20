# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self, root: Optional[TreeNode]) -> None:
        # Mirror Tree
        if root != None :
            root.left, root.right = root.right, root.left
            self.mirror(root.left)
            self.mirror(root.right)
    def move_high_values(self, root: Optional[TreeNode]) -> None:
        # Recursion to move higher values to the lowest leaf
        if root != None :
            # First move the lower values
            self.move_high_values(root.right)
            # Second move itself
            if root.left != None :
                next_node = root.left
                root.left = None
                iterator = root
                while iterator.right != None :
                    iterator = iterator.right
                iterator.right = next_node
                # Third move the other children of this node
                self.move_high_values(next_node)
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Mirror the tree to have the values ordered in right child
        self.mirror(root)
        # Recursively move the left children to be the last leaf
        self.move_high_values(root)
        return root
        
