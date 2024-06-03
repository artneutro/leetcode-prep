# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Definition created to recursively check if the solution was found
    def kthLookUp(self, root: Optional[TreeNode], k: int, solution: List[int]) -> List[int]:
        if root != None and not solution[1]:
            self.kthLookUp(root.left, k, solution)
            solution[0] += 1
            # Once the counter in InOrder traversal match k then mark as found
            if k == solution[0] and solution[2] == -1 :
                solution[1] = True
                solution[2] = root.val
            if not solution[1] :
                self.kthLookUp(root.right, k, solution)
        return solution
    # Use an array with a counter, a boolean found mark and the solution
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        solution = [0, False, -1]
        self.kthLookUp(root, k, solution) 
        return solution[2]

