# https://leetcode.com/problems/partition-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Point to head of each partition list
        solution_low = None
        solution_hig = None
        # Iterate over each partition list
        new_list_low = None
        new_list_hig = None
        # Check for lower or higher values to assign to each partition 
        while (head != None) :
            new_node = ListNode(head.val)
            if head.val < x :
                if new_list_low == None :
                    new_list_low = new_node
                    solution_low = new_list_low
                else :
                    new_list_low.next = new_node
                    new_list_low = new_list_low.next
            else :
                if new_list_hig == None :
                    new_list_hig = new_node
                    solution_hig = new_list_hig
                else :
                    new_list_hig.next = new_node
                    new_list_hig = new_list_hig.next
            head = head.next
        # If no lowers, return highers
        if solution_low == None :
            solution_low = solution_hig
        # Merge both partitions
        else :
            new_list_low.next = solution_hig
        return solution_low

