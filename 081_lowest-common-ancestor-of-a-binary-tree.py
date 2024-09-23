# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Variables initialization
        next_node = None
        # Base case
        if root.val == p.val or root.val == q.val :
            return root
        else :
            # One FIFO queue for BFS and one array to store path to nodes
            fifo = []
            found = []
            # Root node
            root_array = [root]
            fifo.append((root, root_array))
            # Iterate until both nodes are found or Tree is over
            while len(fifo) > 0 and len(found) < 2 :
                next_node = fifo.pop(0)
                if next_node[0].val == p.val or next_node[0].val == q.val :
                    if len(found) > 0 :
                        if next_node[0].val != found[0][0].val :
                        # If node is not in found list, store it
                            found.append(next_node)
                    else :
                        found.append(next_node)
                # If node not found, append children to FIFO queue
                if next_node[0].left != None :
                    # Left check and enqueue
                    if next_node[0].left.val == p.val or next_node[0].left.val == q.val :
                        # Optimization to avoid one level check
                        this_node_array_left = next_node[1].copy()
                        this_node_array_left.append(next_node[0].left)
                        if len(found) == 1 :
                            if next_node[0].val != found[0][0].val :
                                found.append((next_node[0].left, this_node_array_left))
                        else :
                            found.append((next_node[0].left, this_node_array_left))
                        fifo.append((next_node[0].left, this_node_array_left))
                    else :
                        this_node_array_left = next_node[1].copy()
                        this_node_array_left.append(next_node[0].left)
                        fifo.append((next_node[0].left, this_node_array_left))
                if next_node[0].right != None :
                    # Right check and enqueue
                    if next_node[0].right.val == p.val or next_node[0].right.val == q.val :
                        # Optimization to avoid one level check
                        this_node_array_right = next_node[1].copy()
                        this_node_array_right.append(next_node[0].right)
                        if len(found) == 1 :
                            if next_node[0].val != found[0][0].val :
                                found.append((next_node[0].right, this_node_array_right))
                        else :
                            found.append((next_node[0].right, this_node_array_right))
                        fifo.append((next_node[0].right, this_node_array_right))
                    else :
                        this_node_array_right = next_node[1].copy()
                        this_node_array_right.append(next_node[0].right)
                        fifo.append((next_node[0].right, this_node_array_right))
            # Look for same node from last to first in the final paths
            if len(found) == 2 :
                index_p = len((found[0])[1])-1
                while index_p >= 0 :
                    index_q = len((found[1])[1])-1
                    while index_q >= 0 :
                        if (found[0][1])[index_p] == (found[1][1])[index_q] :
                            return found[0][1][index_p]
                        index_q -= 1
                    index_p -= 1
        return None
        
