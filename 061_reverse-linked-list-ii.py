# https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # No changes needed
        if left == right :
            return head
        # Solution variables
        solution = None
        solution_iterator = None
        # Process from start to left
        index = 1
        while index < left :
            # Create a new node and attach to solution
            if solution == None :
                solution = ListNode(head.val)
                solution_iterator = solution
            else :
                solution_iterator.next = ListNode(head.val)
                solution_iterator = solution_iterator.next
            head = head.next
            index += 1
        # Process from left to right
        current_node = None
        next_node = None
        link_node = None
        if head != None :
            current_node = ListNode(head.val)
            link_node = current_node
            head = head.next
        # Create a new node and move the current as its next each time
        while index < right and head != None :
            next_node = ListNode(head.val)
            next_node.next = current_node
            current_node = next_node
            head = head.next
            index += 1
        if solution != None :
            solution_iterator.next = current_node
        else :
            # Case left is 1
            if current_node == None :
                return head
            else :
                # Case right is left+1
                solution = current_node
        # Process after right
        if link_node != None :
            link_node.next = head
        else :
            # Case right is last node or same as left or left+1
            if current_node == None :
                return head
        return solution

