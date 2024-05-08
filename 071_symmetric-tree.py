# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    # Check if 2 trees are the same
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p != None and q != None :
            if p.val == q.val :
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else :
                return False
        elif p == None and q == None :
            return True
        else :
            return False
    # Mirror a tree using its root
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None :
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    # Check if a tree is symmetric on its root using the previous 2 definitions
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root != None :
            if self.isSameTree(self.invertTree(root.left), root.right) :
                return True
        return False
        
