# https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None :
            return head
        else :
            solution = None
            old_pointers = {}
            new_pointers = {}
            count = 0
            # First round => Get nodes, create nodes, get pointers
            head_iterator = head
            current_node = Node(head_iterator.val)
            solution = current_node
            # First iteration
            old_pointers[id(head_iterator)] = count
            head_iterator = head_iterator.next
            count += 1
            while head_iterator != None :
                old_pointers[id(head_iterator)] = count
                next_node = Node(head_iterator.val)
                current_node.next = next_node
                head_iterator = head_iterator.next
                current_node = current_node.next
                count += 1
            # Second round => Assign pointers
            head_iterator = head
            solu_iterator = solution
            solu_internal = solution
            while head_iterator != None and solu_iterator != None :
                if head_iterator.random != None :
                    old_index = old_pointers[id(head_iterator.random)]
                    # O(n2)
                    index = 0
                    while index < old_index :
                        solu_internal = solu_internal.next
                        index += 1
                    solu_iterator.random = solu_internal
                head_iterator = head_iterator.next
                solu_iterator = solu_iterator.next
                solu_internal = solution
            return solution
        
