# https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = []
        self.curr = None
        # Initialize the structure of pointers with O(h) memory
        pointer = root
        while pointer != None :
            # Store all left nodes
            self.tree.append(pointer)
            pointer = pointer.left

    def next(self) -> int:
        # Return the last value in stack
        next_val = self.tree[-1].val
        if self.tree[-1].right != None :
            pointer = self.tree[-1].right
            self.tree.pop()
            # Re-fill with the right nodes of the lower node
            while pointer != None :
                self.tree.append(pointer)
                pointer = pointer.left
        else :
            self.tree.pop()
        return next_val

    def hasNext(self) -> bool:
        # If the stack has values, next exists
        return (len(self.tree) > 0)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

