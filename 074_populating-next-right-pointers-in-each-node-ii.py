# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None :
            return root
        fifo = []
        level_table = {}
        # FIFO using the level, so it can point to the next of that level
        fifo.append((root, 0))
        while len(fifo) > 0 :
            next_node = fifo.pop(0)
            if next_node[1] in level_table :
            # If the level is already in the hashmap, modify the next of last node to the current node
                (level_table[next_node[1]])[-1].next = next_node[0]
                level_table[next_node[1]].append(next_node[0])
            else :
            # If the level is not in the hashmap, create an entry 
                level_table[next_node[1]] = [next_node[0]]
            # Add both children to the FIFO queue, left always first
            if next_node[0].left != None :
                fifo.append((next_node[0].left, next_node[1]+1))
            if next_node[0].right != None :
                fifo.append((next_node[0].right, next_node[1]+1))
        # Return same Tree after modifications
        return root

