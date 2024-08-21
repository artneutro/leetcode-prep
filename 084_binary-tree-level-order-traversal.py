# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def appendNodes(self, root: Optional[TreeNode], level: int, storage: int) -> List[List[int]]:
        solution = []
        cur_level = 0
        cur_nodes = []
        # Iteratively use a queue to store and get the nodes with related level
        if root != None :
            storage.append((level, root))
            while len(storage) > 0 :
                new_level = storage[0][0]
                new_node = storage[0][1]
                # Once the level changes, proceed to append the previous level nodes to solution
                if new_level > cur_level :
                    solution.append(cur_nodes)
                    cur_nodes = [new_node.val]
                    cur_level = new_level
                else :
                    cur_nodes.append(new_node.val)
                # Do the same for children
                if new_node.left != None :
                    storage.append((new_level+1, new_node.left))
                if new_node.right != None :
                    storage.append((new_level+1, new_node.right))
                storage.pop(0)
        if len(cur_nodes) > 0 :
            solution.append(cur_nodes)
        return solution
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Return the iterative solution using a queue including the level as parameter
        return self.appendNodes(root, 0, [])


